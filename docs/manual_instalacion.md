# Manual de instalación

Este manual describe cómo desplegar el sistema en un equipo Windows para propósitos de demostración académica.

## Requisitos previos

| Software | Versión | Enlace |
|---|---|---|
| Node.js | 20 o superior | https://nodejs.org |
| InfluxDB | 1.12 | https://portal.influxdata.com/downloads/ |
| Ollama | última estable | https://ollama.com/download |
| Navegador | Chrome o Edge actualizado | - |

## Instalación paso a paso

### 1. Instalar Node.js y Node-RED

```bash
npm install -g --unsafe-perm node-red
```

Verificar:

```bash
node-red --version
```

### 2. Instalar los nodos de terceros

Iniciar Node-RED con `node-red` en una terminal. Abrir `http://localhost:1880`.

Desde el menú superior derecho → Manage palette → Install, instalar:

- `node-red-dashboard`
- `node-red-contrib-influxdb`
- `node-red-contrib-ui-svg`

### 3. Instalar InfluxDB

Descargar la versión 1.12 desde el enlace oficial e iniciar el servicio.

Crear la base de datos:

```bash
influx
> CREATE DATABASE cacao_monitoreo
> exit
```

### 4. Instalar Ollama y el modelo

Instalar Ollama y descargar el modelo:

```bash
ollama pull qwen2.5:1.5b
```

Verificar:

```bash
ollama list
```

### 5. Importar el flow del sistema

1. Abrir el editor de Node-RED en `http://localhost:1880`.
2. Menú → Import → seleccionar `node-red/flows.json` del repositorio.
3. Confirmar y hacer Deploy.

### 6. Preparar los datos del ensayo

Copiar el archivo `datos/ensayo_santo_domingo/fermentacion_para_nodero.csv` a:
