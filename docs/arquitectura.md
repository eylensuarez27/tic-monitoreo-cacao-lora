# Arquitectura del sistema

## Vista general

El sistema se estructura en cuatro capas siguiendo el modelo IoT clásico:

1. **Capa de percepción**: nodos sensores en campo
2. **Capa de red**: comunicación LoRaWAN
3. **Capa de soporte**: procesamiento y almacenamiento
4. **Capa de aplicación**: HMI y análisis post-proceso

## Componentes principales

### Capa de percepción

- Microcontrolador Heltec LoRa 32 V3 (ESP32-S3 + SX1262)
- Sensor de temperatura DS18B20 con encapsulado IP67
- Sensor de humedad SHT31 de Sensirion
- Módulo RTC DS3231
- Alimentación por batería Li-Po 3.7V 3000 mAh con panel solar 5V/1W
- Controlador de carga TP4056

### Capa de red

- Banda: US915 (autorizada por ARCOTEL Ecuador)
- Factor de propagación: SF10
- Ancho de banda: 125 kHz
- Tamaño de paquete: menos de 50 bytes
- Frecuencia de muestreo: cada 15 minutos
- Encriptación: AES-128

### Capa de soporte

- Gateway: Raspberry Pi con chip SX1302
- Servidor LoRaWAN: ChirpStack local
- Base de datos: InfluxDB 1.12 (`cacao_monitoreo`)
- Procesamiento: Node-RED
- Protocolo interno: MQTT

### Capa de aplicación

- HMI: Node-RED Dashboard
- Cuatro perfiles de usuario con acceso diferenciado
- Ocho pantallas funcionales
- Modo dual de operación (Simulado / Real)
- Sistema híbrido de análisis con Ollama + Qwen 2.5

## Sistema híbrido de análisis

El módulo de análisis post-proceso opera en tres capas:

1. **Sistema experto**: reglas heurísticas cuantitativas que evalúan cuatro criterios (pH final, duración, temperatura máxima, estabilidad térmica).
2. **LLM local**: Qwen 2.5 vía Ollama, que reescribe las recomendaciones del sistema experto para mejorar su fluidez.
3. **Fallback automático**: si el LLM no responde o genera contenido inválido, el sistema utiliza directamente la salida del sistema experto.

Cada recomendación incluye un campo de trazabilidad que cita el criterio cuantitativo que la justifica.

## Consumo energético del nodo

| Estado | Consumo estimado |
|---|---|
| Deep sleep | ~10 µA |
| Lectura de sensores | ~40 mA (2 s) |
| Transmisión LoRa | ~120 mA (300 ms) |
| Ciclo completo cada 15 min | promedio ~50 µA |

Con batería de 3000 mAh y panel solar de 5V/1W, la autonomía teórica es indefinida en condiciones de radiación normal.
