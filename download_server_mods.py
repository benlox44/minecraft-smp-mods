#!/usr/bin/env python3
"""
Downloads or updates server mods from packwiz .pw.toml files.
Usage:
    python download_server_mods.py [--dest PATH]
"""
import argparse
import hashlib
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENV_FILE = ROOT / ".env"
MODS_DIR = ROOT / "mods"


def load_env(env_file: Path) -> dict[str, str]:
    """Load key-value pairs from a simple .env file."""
    env = {}
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#") or "=" not in s:
                continue
            k, _, v = s.partition("=")
            env[k.strip()] = v.strip().strip("'\"")
    return env


def resolve_destination(explicit_dest: Path | None) -> Path:
    """
    Resolve the server mods destination directory with fail-fast validation.
    Priority:
      1. Explicit CLI argument (--dest)
      2. Environment variable or .env file (SERVER_MODS_DEST)
      3. Auto-detected server directory candidates
    """
    # 1. CLI argument
    if explicit_dest:
        dest = explicit_dest.resolve()
        if not dest.exists() and not dest.parent.exists():
            print(f"[ERROR] Destination path is invalid: '{dest}'", file=sys.stderr)
            print(f"[ERROR] Parent directory '{dest.parent}' does not exist.", file=sys.stderr)
            sys.exit(1)
        return dest

    # 2. .env file or environment variable
    env = load_env(ENV_FILE)
    dest_str = env.get("SERVER_MODS_DEST") or os.environ.get("SERVER_MODS_DEST")
    if dest_str:
        dest = Path(dest_str.strip()).resolve()
        if not dest.exists() and not dest.parent.exists():
            print(f"[ERROR] SERVER_MODS_DEST configured in .env is invalid: '{dest}'", file=sys.stderr)
            print(f"[ERROR] Neither '{dest}' nor its parent directory '{dest.parent}' exists.", file=sys.stderr)
            print("[HINT] Verify the path set in your .env file or ensure the target drive is mounted.", file=sys.stderr)
            sys.exit(1)
        return dest

    # 3. Auto-detected fallback candidates
    candidates = [
        Path(r"S:\minecraft-server\data\mods"),
        Path(r"C:\minecraft-server\data\mods"),
        ROOT.parent / "minecraft-server" / "data" / "mods",
    ]
    for c in candidates:
        if c.exists() or c.parent.exists():
            print(f"[*] Auto-detected server mods destination: {c}")
            return c

    # Fail fast if no candidate is found
    print("[ERROR] Could not automatically locate a Minecraft server 'data/mods' directory.", file=sys.stderr)
    print("[HINT] Create a .env file with SERVER_MODS_DEST=<path> or pass --dest <path>.", file=sys.stderr)
    sys.exit(1)


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
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            if current_section:
                data[f"{current_section}.{k}"] = v
            else:
                data[k] = v
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

    if dest.exists() and not dest.is_dir():
        print(f"[ERROR] Destination path is a file, not a directory: '{dest}'", file=sys.stderr)
        sys.exit(1)

    try:
        dest.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"[ERROR] Cannot create destination directory '{dest}': {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Destination: {dest}")

    if not MODS_DIR.is_dir():
        print(f"[ERROR] Mods metadata directory not found: '{MODS_DIR}'", file=sys.stderr)
        sys.exit(1)

    server_mods = []
    for toml_path in sorted(MODS_DIR.glob("*.pw.toml")):
        data = parse_pw_toml(toml_path)
        side = data.get("side", "both")
        if side in ("both", "server"):
            server_mods.append({
                "name": data.get("name", toml_path.stem),
                "filename": data.get("filename", ""),
                "url": data.get("download.url", ""),
                "sha512": data.get("download.hash", ""),
            })

    print(f"[*] Found {len(server_mods)} server/both mods in packwiz metadata.")
    downloaded = 0
    skipped = 0

    for m in server_mods:
        target_file = dest / m["filename"]
        if target_file.exists() and verify_hash(target_file, m["sha512"]):
            skipped += 1
            continue

        print(f"[*] Downloading {m['filename']}...")
        try:
            req = urllib.request.Request(m["url"], headers={"User-Agent": "minecraft-smp-mods-sync/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp, open(target_file, "wb") as out_file:
                while chunk := resp.read(65536):
                    out_file.write(chunk)
        except Exception as exc:
            if target_file.exists():
                target_file.unlink(missing_ok=True)
            print(f"[ERROR] Download failed for {m['filename']}: {exc}", file=sys.stderr)
            sys.exit(1)

        if not verify_hash(target_file, m["sha512"]):
            target_file.unlink(missing_ok=True)
            print(f"[ERROR] Hash mismatch for {m['filename']} (expected {m['sha512']}). Corrupted file removed.", file=sys.stderr)
            sys.exit(1)

        downloaded += 1

    print(f"[+] Completed successfully: {downloaded} downloaded, {skipped} up to date.")


if __name__ == "__main__":
    main()
