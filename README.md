# SMP Minecraft Mods 🛠️

Este repositorio contiene la colección de mods utilizada para nuestro servidor SMP (Survival Multiplayer). El modpack está diseñado para mejorar el rendimiento, la estética y la interacción social sin alterar drásticamente la jugabilidad "vanilla" de Minecraft.

## 📋 Información General

- **Versión de Minecraft:** `1.21.11`
- **Modloader:** [Fabric](https://fabricmc.net/)
- **Fecha de Actualización:** Enero 2026

## 📂 Contenido del Repositorio

El proyecto está dividido en dos carpetas principales para facilitar la instalación:

- **`/client`**: Mods necesarios para los jugadores. Incluye optimizaciones gráficas (Iris, Sodium), mejoras de interfaz y chat de voz.
- **`/server`**: Mods que se ejecutan en el servidor. Incluye optimizaciones de rendimiento (Lithium, C2ME), gestión de permisos y utilidades de administración.

## 🧩 Lista de Mods Destacados

### 🚀 Rendimiento y Optimización (Client & Server)
Mods dedicados a mejorar los FPS, reducir el lag y optimizar el uso de memoria.
- **Sodium** (Client): Motor de renderizado moderno para altos FPS.
- **Lithium** (Server): Optimización general de lógicas del juego.
- **C2ME** (Server): Generación de chunks concurrente para reducir tirones al explorar.
- **FerriteCore**: Reducción del uso de memoria RAM.
- **ScalableLux**: Optimización del motor de iluminación (fork moderno de Starlight).
- **ServerCore** & **Entity View Distance**: Mejoras en el rendimiento del servidor.
- **Spark**: Herramienta de diagnóstico para monitorizar el rendimiento y lag.

### 🎨 Gráficos y Estética (Client)
Mejoras visuales para una experiencia más inmersiva.
- **Iris**: Soporte para Shaders.
- **Distant Horizons**: Permite ver terrenos a distancias extremas sin bajar el rendimiento.
- **Visuality**: Añade partículas cosméticas a eventos del juego.
- **LambDynamicLights**: Iluminación dinámica (antorchas en mano iluminan).
- **Not Enough Animations**: Añade animaciones en tercera persona (comer, navegar, etc.).
- **Sound Physics Perfected**: Simulación física del sonido, ecos y reverberación.
- **LeaveMyBarsAlone**: Evita que otros mods muevan las barras de la interfaz.

### 🗣️ Comunicación y Social
Herramientas para interactuar con otros jugadores.
- **Simple Voice Chat**: Chat de voz por proximidad en el juego.
- **Voice Messages**: Envío de grabaciones de voz.
- **Simple Discord Link**: Conecta el chat del juego con Discord.
- **Chat Heads**: Muestra la cabeza del jugador junto a sus mensajes en el chat.
- **No Chat Reports**: Privacidad y seguridad en el chat.
- **Ping Wheel**: Sistema de ping visual (estilo Apex/Fortnite) para señalar cosas.
- **No Telemetry**: Desactiva el envío de datos de telemetría a Mojang.
- **Locator (Heads & Lodestones)**: Localizador visual de jugadores y piedras imán.

### 🛠️ Utilidades y Calidad de Vida (QoL)
Pequeños cambios que mejoran la experiencia de usuario.
- **JourneyMap**: Mapa en tiempo real y minimapa.
- **AppleSkin**: Visualización de saturación y hambre.
- **DeathFinder & DeathBackup**: Ayuda para recuperar items tras morir.
- **Image2Map**: Permite importar imágenes al juego como mapas.
- **Audioplayer**: Reproducción de música personalizada mediante discos/cajas de música.
- **ServerSleep**: Permite pasar la noche si un porcentaje de jugadores duerme.
- **CutThrough**: Permite interactuar con cofres/letreros a través de marcos (sustituye a ClickThrough).
- **BetterStats**: Interfaz de estadísticas mejorada y organizada.
- **ShulkerBoxTooltip**: Ver el contenido de cajas de shulker desde el inventario.
- **Scribble**: Permite dibujar y tomar notas en los mapas.
- **vt-downloader**: Descargador de recursos de Vanilla Tweaks integrado.

## 💾 Instalación

### Para Jugadores (Cliente)
1. Instala **Minecraft 1.21.11**.
2. Instala el cargador de mods **Fabric**.
3. Descarga el contenido de la carpeta `client/`.
4. Copia todos los archivos `.jar` en tu carpeta `.minecraft/mods`.
   - *Nota: Si usas Prism Launcher o Modrinth App, simplemente crea una instancia Fabric 1.21.11 y arrastra los mods.*

### Para Administradores (Servidor)
1. Configura un servidor con **Fabric** para la versión 1.21.11.
2. Copia los archivos de la carpeta `server/` a la carpeta `mods` de tu servidor.
3. Reinicia el servidor para generar las configuraciones.

## ⚠️ Notas Importantes
- **Java**: Asegúrate de tener instalado Java 21 (o la versión requerida por 1.21.11 en 2026).
- **Configuración**: Algunos mods como `Distant Horizons` requieren configuración adicional en el cliente para funcionar óptimamente según tu PC.

Resourse Pack recomendado: https://vanillatweaks.net/share#ekNtf1