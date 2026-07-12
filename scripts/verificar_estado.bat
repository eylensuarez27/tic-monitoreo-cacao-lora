@echo off
title Verificar Estado - Sistema Cacao
echo ========================================
echo  Verificando estado de los servicios
echo ========================================
echo.

echo [1] InfluxDB (puerto 8086):
netstat -an | findstr :8086 | findstr LISTENING >nul && (echo    Corriendo) || (echo    NO corriendo)
echo.

echo [2] Ollama (puerto 11434):
netstat -an | findstr :11434 | findstr LISTENING >nul && (echo    Corriendo) || (echo    NO corriendo)
echo.

echo [3] Node-RED (puerto 1880):
netstat -an | findstr :1880 | findstr LISTENING >nul && (echo    Corriendo) || (echo    NO corriendo)
echo.

echo ========================================
echo  Modelos disponibles en Ollama:
echo ========================================
ollama list
echo.

pause