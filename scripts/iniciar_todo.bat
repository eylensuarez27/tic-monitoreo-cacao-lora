@echo off
title Sistema Cacao - Iniciador
echo ========================================
echo  Sistema de Monitoreo IoT Cacao
echo  Trabajo de Integracion Curricular EPN
echo ========================================
echo.
echo Iniciando los tres servicios en ventanas separadas...
echo.

echo [1/3] Iniciando InfluxDB...
start "InfluxDB - Sistema Cacao" cmd /k "influxd"
timeout /t 3 /nobreak >nul

echo [2/3] Iniciando Ollama...
start "Ollama - Sistema Cacao" cmd /k "ollama serve"
timeout /t 3 /nobreak >nul

echo [3/3] Iniciando Node-RED...
start "Node-RED - Sistema Cacao" cmd /k "node-red"
timeout /t 5 /nobreak >nul

echo.
echo ========================================
echo  Todos los servicios iniciados
echo ========================================
echo.
echo  InfluxDB:  http://localhost:8086
echo  Ollama:    http://localhost:11434
echo  Node-RED:  http://localhost:1880
echo  Dashboard: http://localhost:1880/ui
echo.
echo Abre http://localhost:1880/ui en tu navegador.
echo.
pause