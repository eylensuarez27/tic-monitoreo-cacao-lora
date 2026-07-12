# Configuración de Ollama con Qwen 2.5

Este directorio contiene la configuración del modelo de lenguaje local utilizado en la capa de análisis post-proceso del sistema.

## Justificación técnica

El sistema utiliza Ollama con el modelo Qwen 2.5 de 1,5 mil millones de parámetros por cuatro razones:

- **Operación offline**: no requiere conectividad a internet.
- **Sin costos recurrentes**: a diferencia de APIs comerciales que cobran por token.
- **Privacidad**: los datos del productor nunca salen del equipo local.
- **Tolerancia a fallos**: si el LLM no responde, el sistema experto continúa operando.

## Instalación

1. Descargar Ollama desde https://ollama.com/download
2. Instalar según el sistema operativo.
3. En una terminal, ejecutar:

```bash
ollama pull qwen2.5:1.5b
```

4. Verificar la instalación:

```bash
ollama list
```

5. El endpoint queda disponible en `http://localhost:11434/api/generate`.

## Verificación rápida

```bash
ollama run qwen2.5:1.5b "Explica en una oración qué es el ácido acético."
```

Para salir del prompt interactivo, escribir `/bye`.

## Requisitos de hardware

| Recurso | Mínimo |
|---|---|
| RAM | 8 GB |
| Espacio en disco | 2 GB (para el modelo) |
| CPU | Cualquier arquitectura x86_64 o ARM64 |
| GPU | No requerida |

## Parámetros del modelo utilizados en el sistema

- `temperature`: 0.4
- `top_p`: 0.85
- `num_predict`: 250
- `stream`: false

Los prompts completos utilizados en el sistema están en la carpeta `prompts/`.
