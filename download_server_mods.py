#!/usr/bin/env python3
"""
Downloads or updates server mods from packwiz .pw.toml files.
Usage:
    python download_server_mods.py [--dest PATH]
"""
import argparse
import glob
import hashlib
import os
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODS_DIR = ROOT / "mods"
DEFAULT_DEST = ROOT.parent / "minecraft-server" / "data" / "mods"


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
    parser.add_argument("--dest", type=Path, default=DEFAULT_DEST, help="Destination directory for server mods")
    args = parser.parse_args()

    dest = args.dest
    dest.mkdir(parents=True, exist_ok=True)
    print(f"[*] Destination: {dest}")

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
        urllib.request.urlretrieve(m["url"], target_file)
        if not verify_hash(target_file, m["sha512"]):
            print(f"[ERROR] Hash mismatch for {m['filename']}")
        else:
            downloaded += 1

    print(f"[*] Completed: {downloaded} downloaded, {skipped} up to date.")


if __name__ == "__main__":
    main()
