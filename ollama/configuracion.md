# Configuración de Ollama en el sistema

## Parámetros del modelo

El sistema utiliza el modelo `qwen2.5:1.5b` con los siguientes parámetros:

| Parámetro | Valor | Justificación |
|---|---|---|
| `temperature` | 0.4 | Reduce la creatividad para mantener el tono técnico |
| `top_p` | 0.85 | Filtra tokens de baja probabilidad |
| `num_predict` | 250 | Limita la extensión de la respuesta |
| `stream` | false | Requiere respuesta completa antes de procesar |

## Endpoint
POST http://localhost:11434/api/generate
Content-Type: application/json
{
"model": "qwen2.5:1.5b",
"prompt": "...",
"stream": false,
"options": {
"temperature": 0.4,
"num_predict": 250,
"top_p": 0.85
}
}

## Estrategia anti-alucinación

### Palabras prohibidas

Si la respuesta contiene alguna de estas palabras, se activa el fallback al sistema base:

- sangre, sanguíneo
- salud, médico, infección, paciente, dosis
- dureza (concepto ajeno al proceso)

### Palabras válidas requeridas

La respuesta debe contener al menos dos de estas palabras del dominio:

- temperatura
- volteo, volteos
- hojas de plátano
- mucílago
- bacterias acéticas
- levaduras
- fermentación
- embrión, grano
- pH, ácido acético

Si la respuesta no cumple con estos filtros, el sistema muestra la salida del sistema experto directamente y etiqueta la fuente como "Sistema base".

## Verificación del servicio

```bash
curl http://localhost:11434/api/tags
```

Debe retornar la lista de modelos instalados incluyendo `qwen2.5:1.5b`.

## Latencia esperada

- CPU Intel UHD: 20-40 segundos por análisis
- CPU con instrucciones AVX2: 10-20 segundos
- GPU dedicada: 2-5 segundos

## Mecanismo de fallback

Si el LLM tarda más de 90 segundos, no responde o genera contenido inválido, el sistema utiliza directamente las recomendaciones del sistema experto y muestra la etiqueta "Sistema base" en la interfaz.
