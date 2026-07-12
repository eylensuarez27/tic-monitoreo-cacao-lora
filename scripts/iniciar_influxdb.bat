@echo off
title InfluxDB - Sistema Cacao
echo ========================================
echo  Iniciando InfluxDB
echo ========================================
echo.
echo InfluxDB estara disponible en http://localhost:8086
echo No cierres esta ventana mientras uses el sistema.
echo.
influxd
pause