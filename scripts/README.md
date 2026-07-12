# Scripts de arranque

Scripts para iniciar los servicios del sistema en Windows.

## Uso

### Iniciar todo de golpe

Doble click en `iniciar_todo.bat`. Se abren tres ventanas de terminal, una para cada servicio:

- InfluxDB en `http://localhost:8086`
- Ollama en `http://localhost:11434`
- Node-RED en `http://localhost:1880`

Luego abre `http://localhost:1880/ui` en el navegador.

### Iniciar servicios individuales

- `iniciar_influxdb.bat`: solo la base de datos
- `iniciar_ollama.bat`: solo el modelo de lenguaje local
- `iniciar_nodered.bat`: solo Node-RED

### Verificar el estado

`verificar_estado.bat`: muestra si cada servicio esta corriendo y lista los modelos disponibles en Ollama.

## Requisitos

Antes de usar los scripts, asegurate de tener instalado y agregado al PATH:

- InfluxDB 1.12
- Ollama con el modelo `qwen2.5:1.5b` descargado
- Node.js 20+ y Node-RED

Para descargar el modelo:

ollama pull qwen2.5:1.5b

## Detener los servicios

Cierra cada ventana con Ctrl+C o simplemente cierra la ventana.