# Metadatos del ensayo complementario

## Información general

| Parámetro | Valor |
|---|---|
| Ubicación | Santo Domingo de los Tsáchilas, Ecuador |
| Fecha de inicio | Domingo 31 de mayo de 2026, 12:40 |
| Fecha de fin | Sábado 6 de junio de 2026, 19:00 |
| Duración total | 6,27 días |
| Masa de cacao | 20 kg |
| Variedad | Cacao Nacional ecuatoriano |
| Fermentador | Tina plástica con cobertura de hojas de plátano |

## Registros

| Parámetro | Valor |
|---|---|
| Registros válidos | 1.805 |
| Frecuencia de muestreo | 5 minutos |
| Duración de la captura | 6,27 días continuos |

## Resultados

| Variable | Valor |
|---|---|
| Temperatura mínima | 27,06 °C |
| Temperatura máxima | 36,63 °C |
| pH inicial | 6,4 |
| pH final | 5,0 |
| Fases identificadas | 4 (Anaerobia, Acética intermedia, Acética final, Descenso) |

## Hardware utilizado

**Nota:** el hardware empleado en este ensayo **no corresponde** al hardware propuesto en el TIC. Se utilizó una solución mínima basada en componentes accesibles localmente.

| Componente | Modelo |
|---|---|
| Microcontrolador | ESP32 (genérico) |
| Sensor de temperatura | DS18B20 con encapsulado de acero |
| Sensor de humedad | YL-100 (con activación intermitente para mitigar electrólisis) |
| Almacenamiento | SPIFFS interno del ESP32 |
| Extracción de datos | Script Python con librería pyserial |

## Observación empírica sobre el sensor YL-100

Durante el ensayo se identificó que el sensor YL-100 no fue compatible con el ambiente químico del proceso de fermentación. Pese a la implementación de una estrategia de activación intermitente en el firmware para mitigar la electrólisis, el sensor sufrió corrosión electroquímica en sus electrodos debido a la exposición al ácido acético producido por las bacterias acéticas durante la fase aerobia.

Este hallazgo refuerza la decisión de diseño del TIC de proponer el sensor SHT31 de Sensirion, con encapsulado y principio de medición capacitivo adecuados al ambiente.

## Reproducibilidad

Este ensayo puede reproducirse cargando el archivo `fermentacion_para_nodero.csv` en Node-RED según se describe en el manual de instalación del sistema.
