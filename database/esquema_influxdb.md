# Esquema de InfluxDB

## Base de datos

Nombre: `cacao_monitoreo`

## Measurements

### 1. `lotes`

Almacena información resumida de cada lote de fermentación.

| Campo | Tipo | Descripción |
|---|---|---|
| `lote_id` | tag | Identificador único (prefijo `lote_sim_` o `lote_real_`) |
| `ph_inicial` | field (float) | pH del cotiledón al inicio |
| `ph_final` | field (float) | pH del cotiledón al final |
| `duracion_horas` | field (integer) | Duración total en horas |
| `temp_max` | field (float) | Temperatura máxima registrada (°C) |
| `temp_min` | field (float) | Temperatura mínima registrada (°C) |
| `cierre_automatico` | field (integer) | 1 si cerró automáticamente, 0 si fue manual |
| `time` | timestamp | Momento de finalización del lote |

### 2. `datos_sensores`

Almacena las lecturas de sensores durante el proceso.

| Campo | Tipo | Descripción |
|---|---|---|
| `lote_id` | tag | Identificador del lote asociado |
| `modo` | tag | `simulado` o `real` |
| `temperatura` | field (float) | Temperatura de la masa (°C) |
| `humedad` | field (float) | Humedad relativa ambiental (%) |
| `tiempo_horas` | field (float) | Tiempo transcurrido desde el inicio (h) |
| `rssi` | field (float) | Intensidad de señal LoRa (dBm) |
| `snr` | field (float) | Relación señal a ruido LoRa (dB) |
| `time` | timestamp | Momento de la lectura |

## Retention Policies

Se recomienda configurar:

- `autogen`: retención por defecto (infinita durante desarrollo)
- Para producción: definir una política de retención de 1 año

## Creación de la base de datos

```bash
influx
> CREATE DATABASE cacao_monitoreo
> USE cacao_monitoreo
> SHOW MEASUREMENTS
```
