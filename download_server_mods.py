#!/usr/bin/env python3
import argparse
import hashlib
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENV_FILE = ROOT / ".env"
MODS_DIR = ROOT / "mods"


def load_env(path: Path) -> dict[str, str]:
    env = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip().strip("'\"")
    return env


def resolve_destination(cli_dest: Path | None) -> Path:
    if cli_dest:
        dest = cli_dest.resolve()
    else:
        env = load_env(ENV_FILE)
        dest_str = env.get("SERVER_MODS_DEST") or os.environ.get("SERVER_MODS_DEST")
        if not dest_str:
            print("[ERROR] SERVER_MODS_DEST not set. Configure it in .env or pass --dest.", file=sys.stderr)
            sys.exit(1)
        dest = Path(dest_str.strip()).resolve()

    if not dest.exists() and not dest.parent.exists():
        print(f"[ERROR] Destination does not exist: '{dest}'", file=sys.stderr)
        sys.exit(1)

    if dest.exists() and not dest.is_dir():
        print(f"[ERROR] Destination is a file, not a directory: '{dest}'", file=sys.stderr)
        sys.exit(1)

    try:
        dest.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"[ERROR] Cannot create destination directory '{dest}': {exc}", file=sys.stderr)
        sys.exit(1)

    return dest


def parse_pw_toml(path: Path) -> dict:
    data = {}
    current_section = None
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current_section = line[1:-1]
            continue
        if "=" in line:
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip("'\"")
            data[f"{current_section}.{k}" if current_section else k] = v
    return data


def verify_hash(file_path: Path, expected_hash: str) -> bool:
    if not file_path.exists():
        return False
    h = hashlib.sha512()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest().lower() == expected_hash.lower()


def main():
    parser = argparse.ArgumentParser(description="Download server mods from packwiz metadata.")
    parser.add_argument("--dest", type=Path, default=None, help="Destination directory for server mods")
    args = parser.parse_args()

    dest = resolve_destination(args.dest)
    print(f"[*] Destination: {dest}")

    if not MODS_DIR.is_dir():
        print(f"[ERROR] Mods directory not found: '{MODS_DIR}'", file=sys.stderr)
        sys.exit(1)

    server_mods = []
    for toml_path in sorted(MODS_DIR.glob("*.pw.toml")):
        data = parse_pw_toml(toml_path)
        if data.get("side", "both") in ("both", "server"):
            server_mods.append({
                "filename": data.get("filename", ""),
                "url": data.get("download.url", ""),
                "sha512": data.get("download.hash", ""),
            })

    print(f"[*] Found {len(server_mods)} server mods in metadata.")
    downloaded = 0
    skipped = 0

    for m in server_mods:
        target = dest / m["filename"]
        if target.exists() and verify_hash(target, m["sha512"]):
            skipped += 1
            continue

        print(f"[*] Downloading {m['filename']}...")
        try:
            req = urllib.request.Request(m["url"], headers={"User-Agent": "minecraft-smp-mods-sync/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp, open(target, "wb") as out:
                while chunk := resp.read(65536):
                    out.write(chunk)
        except Exception as exc:
            if target.exists():
                target.unlink(missing_ok=True)
            print(f"[ERROR] Download failed for {m['filename']}: {exc}", file=sys.stderr)
            sys.exit(1)

        if not verify_hash(target, m["sha512"]):
            target.unlink(missing_ok=True)
            print(f"[ERROR] Hash mismatch for {m['filename']}.", file=sys.stderr)
            sys.exit(1)

        downloaded += 1

    print(f"[+] Completed: {downloaded} downloaded, {skipped} up to date.")


if __name__ == "__main__":
    main()
