# Queries de ejemplo para InfluxDB

Ejemplos útiles para consultar datos del sistema.

## Listar todos los lotes disponibles

```sql
SELECT lote_id, ph_inicial, ph_final, duracion_horas, temp_max, temp_min
FROM lotes
ORDER BY time DESC
```

## Consultar datos de un lote específico

```sql
SELECT temperatura, humedad, tiempo_horas
FROM datos_sensores
WHERE lote_id = 'lote_real_2026-05-31T12-40-00'
ORDER BY time ASC
```

## Obtener estadísticas de temperatura de un lote

```sql
SELECT MAX(temperatura) AS temp_max, 
       MIN(temperatura) AS temp_min, 
       MEAN(temperatura) AS temp_prom
FROM datos_sensores
WHERE lote_id = 'lote_real_2026-05-31T12-40-00'
```

## Contar lotes por tipo

```sql
SELECT COUNT(lote_id) AS total
FROM lotes
WHERE lote_id =~ /^lote_real_/
```

```sql
SELECT COUNT(lote_id) AS total
FROM lotes
WHERE lote_id =~ /^lote_sim_/
```

## Última lectura de un lote activo

```sql
SELECT last(temperatura), last(humedad), last(rssi), last(snr)
FROM datos_sensores
WHERE lote_id = 'lote_sim_actual'
```

## Datos LoRa de los últimos 7 días

```sql
SELECT rssi, snr
FROM datos_sensores
WHERE time > now() - 7d
ORDER BY time DESC
```

## Eliminar un lote de prueba

```sql
DELETE FROM lotes WHERE lote_id = 'lote_sim_test'
DELETE FROM datos_sensores WHERE lote_id = 'lote_sim_test'
```
