# Sistema de Monitoreo IoT basado en LoRa para Fermentación de Cacao

Trabajo de Integración Curricular (TIC) — Escuela Politécnica Nacional, Ecuador.

## Descripción

Sistema de monitoreo diseñado para supervisar el proceso de fermentación del cacao mediante comunicación LoRa. El componente integra adquisición de datos, comunicación inalámbrica de largo alcance, almacenamiento en base de datos de series temporales, visualización mediante HMI y análisis post-proceso con un enfoque híbrido de reglas y modelo de lenguaje local.

## Información académica

| Campo | Detalle |
|---|---|
| Universidad | Escuela Politécnica Nacional (EPN) |
| Facultad | Facultad de Ingeniería Eléctrica y Electrónica |
| Carrera | Ingeniería en Electrónica y Automatización |
| Estudiante | Eylen Daniela Suárez Alegría |
| Director | Dr. Danilo Chávez |
| Año | 2026 |

## Características principales

- Arquitectura IoT en cuatro capas: percepción, red, soporte y aplicación.
- Comunicación LoRaWAN en banda US915, apropiada para Ecuador según ARCOTEL.
- HMI con cuatro perfiles de usuario: Agricultor, Jefe de planta, Técnico LoRa y Administrador.
- Modo dual de operación: simulado y real, con datos del ensayo complementario.
- Sistema híbrido de análisis: reglas heurísticas cuantitativas más Qwen 2.5 vía Ollama.
- Alarmas diferenciadas por dominio: proceso y comunicación separadas por rol.
- Trazabilidad académica: cada recomendación cita el criterio cuantitativo que la justifica.
- Diseño HMI bajo norma ISA-101 de alto desempeño.

## Stack técnico

| Componente | Tecnología |
|---|---|
| Programación visual | Node-RED |
| Base de datos | InfluxDB 1.12 |
| Servidor LoRaWAN | ChirpStack |
| Protocolo de mensajería | MQTT con AES-128 |
| Modelo de lenguaje local | Ollama + Qwen 2.5 (1.5B) |
| Norma de HMI | ANSI/ISA-101.01-2015 |
| Banda LoRa | US915 |

## Estructura del repositorio

tic-monitoreo-cacao-lora/
├── docs/           Documentación del sistema
├── node-red/       Flow completo de Node-RED
├── ollama/         Configuración y prompts del LLM
├── datos/          CSV del ensayo complementario
├── database/       Esquemas y queries InfluxDB
├── diagramas/      Diagramas de arquitectura y flujo
├── capturas/       Screenshots del HMI en operación
└── documento/      Documento final del TIC
## Ensayo complementario

Como mecanismo auxiliar para enriquecer la validación del HMI con perfiles térmicos realistas, se ejecutó un ensayo de captura de datos en Santo Domingo de los Tsáchilas, del 31 de mayo al 6 de junio de 2026. Este ensayo no forma parte del alcance del TIC; su propósito fue únicamente alimentar el modo Real del HMI con registros de una fermentación real.

| Parámetro | Valor |
|---|---|
| Ubicación | Santo Domingo de los Tsáchilas, Ecuador |
| Duración | 6,27 días |
| Masa | 20 kg de cacao Nacional ecuatoriano |
| Registros | 1.805 lecturas válidas |
| Frecuencia | Muestra cada 5 minutos |
| Rango térmico | 27,06 °C a 36,63 °C |
| Descenso de pH | 6,4 → 5,0 |

## Instalación rápida

1. Instalar Node.js 20+ y Node-RED.
2. Instalar InfluxDB 1.12 y crear la base de datos `cacao_monitoreo`.
3. Instalar Ollama y descargar el modelo `qwen2.5:1.5b`.
4. Importar el archivo `node-red/flows.json` en el editor de Node-RED.
5. Acceder al dashboard en `http://localhost:1880/ui`.

Detalles en `docs/manual_instalacion.md`.

## Credenciales de demostración

| Rol | Usuario | Contraseña |
|---|---|---|
| Agricultor | agricultor | cacao123 |
| Jefe de planta | jefe | jefe123 |
| Técnico LoRa | tecnico | tecnico123 |
| Administrador | admin | admin123 |

Estas credenciales son solo para propósitos de demostración académica.

## Licencia

Este proyecto se distribuye bajo licencia MIT. Consulte el archivo `LICENSE` para más detalles.

## Contacto

Para consultas académicas relacionadas con este trabajo:

- Estudiante: eylen.suarez@epn.edu.ec
- Director: danilo.chavez@epn.edu.ec

---

Escuela Politécnica Nacional — 2026
