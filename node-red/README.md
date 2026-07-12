# Flow de Node-RED

Este directorio contiene el flow completo del sistema de monitoreo implementado en Node-RED.

## Requisitos

- Node.js 20 o superior
- Node-RED 3.x o superior
- InfluxDB 1.12
- Ollama con el modelo `qwen2.5:1.5b` disponible en `http://localhost:11434`

## Nodos externos utilizados

Antes de importar el flow, instalar en la paleta de Node-RED:

- `node-red-dashboard`
- `node-red-contrib-influxdb`
- `node-red-contrib-ui-svg`

## Importación del flow

1. Abrir Node-RED en `http://localhost:1880`.
2. Menú superior derecho → Import.
3. Seleccionar el archivo `flows.json` de este directorio.
4. Confirmar la importación en el flujo actual.
5. Deploy.
6. Abrir el dashboard en `http://localhost:1880/ui`.

## Estructura del flow

- **Pantalla Portada**: entrada del sistema.
- **Pantalla Login**: autenticación con selector de modo Simulado/Real.
- **Pantalla Agricultor - Lote actual**: operación del proceso.
- **Pantalla Jefe - Monitoreo**: supervisión en tiempo real.
- **Pantalla Jefe - Históricos**: análisis post-proceso con sistema híbrido.
- **Pantalla Jefe - Comparación**: comparación cuantitativa entre lotes.
- **Pantalla Técnico - LoRa**: monitoreo del enlace inalámbrico.
- **Pantalla Admin**: panel central con acceso a todas las vistas.

## Variables globales relevantes

- `modo_fuente`: define el modo activo (`simulado` o `real`).
- `lotes_disponibles_comp`: cache de lotes disponibles para comparación.
- `log_alarmas`: registro de alarmas de proceso.
- `log_alarmas_lora`: registro de alarmas de comunicación.
