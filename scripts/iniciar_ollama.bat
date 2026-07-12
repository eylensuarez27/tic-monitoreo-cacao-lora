@echo off
title Ollama - Sistema Cacao
echo ========================================
echo  Iniciando Ollama con Qwen 2.5
echo ========================================
echo.
echo Ollama estara disponible en http://localhost:11434
echo Modelo cargado: qwen2.5:1.5b
echo No cierres esta ventana mientras uses el sistema.
echo.
ollama serve
pause