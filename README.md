# Minecraft SMP Mods 

Collection of mods used in our SMP server for Minecraft 26.3 (Fabric). Managed with [packwiz](https://packwiz.infra.link/) and distributed as a modern [Modrinth Modpack (`.mrpack`)](https://modrinth.com/).

## Installation (Client)

### Option 1: Prism Launcher (Recommended)
1. Download `minecraft-smp-mods.mrpack` from the [Releases](https://github.com/benlox44/minecraft-smp-mods/releases) page.
2. Open [Prism Launcher](https://prismlauncher.org/).
3. Click **"Add Instance"** -> **"Import"**.
4. Select `minecraft-smp-mods.mrpack` and confirm.
5. Launch the game!

### Option 2: Modrinth App
1. Download `minecraft-smp-mods.mrpack`.
2. In the Modrinth App, click the **+** (Add Profile) -> **Import from file**.
3. Select `minecraft-smp-mods.mrpack` and launch.

---

## Server Synchronization

To download or update the server-side mods directly into `minecraft-server/data/mods`:

```bash
just sync-server
# or directly:
python download_server_mods.py
```

---

## Modpack Management (for maintainers)

This repository uses **packwiz** with `.pw.toml` files pointing to Modrinth, keeping the Git repository lightweight without storing binary `.jar` files:

- `just refresh`: Refreshes the packwiz index (`index.toml`).
- `just export`: Exports a new `minecraft-smp-mods.mrpack` to upload to GitHub Releases.
- `just update`: Automatically checks and updates all mods to their latest versions on Modrinth.
- `just sync-server`: Downloads/syncs all server mods to `minecraft-server/data/mods`.

---

## Content Mods

### Client & Visuals
- [AppleSkin](https://modrinth.com/mod/appleskin): Shows food exhaustion and saturation on the HUD.
- [Better Mount HUD](https://modrinth.com/mod/better-mount-hud): Improves the HUD information when riding horses and other mounts.
- [Better Statistics Screen](https://modrinth.com/mod/better-statistics-screen): Replaces the statistics screen with an easier to use and read layout.
- [Boat Item View](https://modrinth.com/mod/boat-item-view): Allows you to see your held items while riding in a boat.
- [Chat Heads](https://modrinth.com/mod/chat-heads): Displays player heads next to their messages in chat.
- [Cut Through](https://modrinth.com/mod/cut-through): Allows hitting entities through transparent blocks like tall grass.
- [Death Finder](https://modrinth.com/mod/death-finder): Prints death coordinates and dimension in the chat upon dying.
- [Elytra Trims](https://modrinth.com/mod/elytra-trims): Enables armor trims to be applied to Elytra wings.
- [Iris Shaders](https://modrinth.com/mod/iris): A modern shaders mod compatible with Sodium.
- [LambDynamicLights](https://modrinth.com/mod/lambdynamiclights): Adds dynamic lighting where held items emit light.
- [Leave My Bars Alone](https://modrinth.com/mod/leave-my-bars-alone): Prevents effects and other factors from shifting the hotbar and HUD.
- [Locator Heads](https://modrinth.com/mod/locator-heads): Displays player heads on the locator bar.
- [MaLiLib](https://modrinth.com/mod/malilib): Configuration library required by masa's client-side mods.
- [MiniHUD](https://modrinth.com/mod/minihud): Highly configurable mini F3-like information overlay.
- [Mod Menu](https://modrinth.com/mod/modmenu): Adds an in-game menu to view and configure installed mods.
- [Not Enough Animations](https://modrinth.com/mod/not-enough-animations): Adds missing third-person animations like eating, drinking, and rowing.
- [Scribble](https://modrinth.com/mod/scribble): Provides advanced book editing tools and formatting options.
- [Shulker Box Tooltip](https://modrinth.com/mod/shulkerboxtooltip): Allows viewing the contents of Shulker Boxes in the inventory.
- [Sodium Shadowy Path Blocks](https://modrinth.com/mod/sodium-shadowy-path-blocks): Fixes a visual bug with shadows on path blocks when using Sodium.
- [Sound Physics Perfected](https://modrinth.com/mod/sound-physics-perfected): Simulates realistic sound attenuation, reverberation, and absorption.
- [Visuality](https://modrinth.com/mod/visuality): Adds visual particle effects for various game events.
- [Voxy](https://modrinth.com/mod/voxy): Lightweight, GPU-driven voxel Level of Detail (LOD) mod for massive render distances.
- [Voxy Server Side](https://modrinth.com/plugin/voxy-server-side): Streams distant terrain LOD data from the server to connected Voxy clients.

### Performance & Optimization
- [C2ME](https://modrinth.com/mod/c2me-fabric): Optimizes chunk generation and loading for better performance.
- [Debugify](https://modrinth.com/mod/debugify): Fixes many vanilla Minecraft bugs on both client and server.
- [FerriteCore](https://modrinth.com/mod/ferrite-core): Reduces memory (RAM) usage significantly.
- [Lithium](https://modrinth.com/mod/lithium): General-purpose optimization mod to improve game logic and physics performance.
- [ScalableLux](https://modrinth.com/mod/scalablelux): Optimizes the lighting engine for better server and world performance.
- [ServerCore](https://modrinth.com/mod/servercore): Comprehensive server optimization and ticking performance enhancements.
- [Sodium](https://modrinth.com/mod/sodium): Rendering engine replacement that greatly improves frame rates.
- [spark](https://modrinth.com/mod/spark): A performance profiling tool for diagnosing lag on client and server.
- [Structure Layout Optimizer](https://modrinth.com/mod/structure-layout-optimizer): Optimizes jigsaw structure generation to reduce server freezes.

### Social & Chat
- [AudioPlayer](https://modrinth.com/mod/audioplayer): Allows playing custom audio files and music discs in the world.
- [More Chat History](https://modrinth.com/mod/more-chat-history): Increases the maximum length of the scrolling chat history.
- [No Chat Reports](https://modrinth.com/mod/no-chat-reports): Disables chat reporting telemetry and crypto-signing.
- [No Telemetry](https://modrinth.com/mod/no-telemetry): Disables telemetry data collection sent to Mojang.
- [Ping Wheel](https://modrinth.com/mod/ping-wheel): Adds a ping wheel system for easy communication of locations.
- [Simple Discord Link](https://modrinth.com/mod/simple-discord-link): Bridges Minecraft chat with a Discord server.
- [Simple Voice Chat](https://modrinth.com/mod/simple-voice-chat): Adds proximity-based voice chat to the game.
- [Styled Chat](https://modrinth.com/mod/styled-chat): Allows customization of the chat format and style.
- [TAB](https://modrinth.com/plugin/tab-was-taken): Enables extensive customization of the tab list.
- [Voice Messages](https://modrinth.com/plugin/voicemessages): Allows sending recorded voice messages in chat.

### Server Utils & World
- [Chunky](https://modrinth.com/mod/chunky): Fast and efficient world pre-generator.
- [Death Backup](https://modrinth.com/mod/death-backup): Automatically backs up player inventories right before death.
- [Entity View Distance](https://modrinth.com/mod/entity-view-distance): Precise control over entity rendering distance on the server.
- [JourneyMap](https://modrinth.com/mod/journeymap): Real-time mapping support and server sync.
- [Lithostitched](https://modrinth.com/mod/lithostitched): Expansive library with enhanced configurability for custom world generation.
- [NetherPortalFix](https://modrinth.com/mod/netherportalfix): Ensures correct destinations when travelling back and forth through Nether Portals.
- [Server Sleep](https://modrinth.com/mod/serversleep): Allows the night to pass when only a percentage of players sleep.
- [Servux](https://modrinth.com/mod/servux): Server-side support and bounding box integration for client mods like MiniHUD.
- [Sessility](https://modrinth.com/mod/sessility): Tracks player AFK state on the server.
- [squaremap](https://modrinth.com/mod/squaremap): Minimalistic, fast web-based live map viewer.
- [View Distance Fix](https://modrinth.com/mod/view-distance-fix): Fixes view distance desync between client and server.
