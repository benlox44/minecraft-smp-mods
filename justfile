set windows-shell := ["cmd.exe", "/c"]

# Show available commands
default:
    @just --list

# Refresh packwiz index after editing or adding .pw.toml files
refresh:
    packwiz refresh

# Export pack to Modrinth .mrpack
export: refresh
    packwiz mr export -o smp-mods.mrpack

# Update all mods to their latest versions on Modrinth
update:
    packwiz update -y

# Sync / download all server mods to the live minecraft-server folder
sync-server:
    python download_server_mods.py
