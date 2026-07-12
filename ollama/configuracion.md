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
