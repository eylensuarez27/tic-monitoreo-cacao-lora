# Sistema de Monitoreo IoT basado en LoRa para Fermentación de Cacao

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-completado-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-Node--RED-red.svg)
![LLM](https://img.shields.io/badge/LLM-Qwen%202.5-orange.svg)

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

- **Arquitectura IoT en cuatro capas**: percepción, red, soporte y aplicación.
- **Comunicación LoRaWAN** en banda US915, apropiada para Ecuador según ARCOTEL.
- **HMI con cuatro perfiles de usuario**: Agricultor, Jefe de planta, Técnico LoRa y Administrador.
- **Modo dual de operación**: simulado y real, con datos del ensayo complementario.
- **Sistema híbrido de análisis**: reglas heurísticas cuantitativas + Qwen 2.5 vía Ollama.
- **Alarmas diferenciadas por dominio**: proceso y comunicación separadas por rol.
- **Trazabilidad académica**: cada recomendación cita el criterio cuantitativo que la justifica.
- **Diseño HMI bajo norma ISA-101** de alto desempeño.

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
