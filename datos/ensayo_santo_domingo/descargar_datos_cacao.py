# ============================================================
#  DESCARGAR DATOS DE LA TESIS DE CACAO
#  Conecta al ESP32 por Serial, envia comando DUMP,
#  recibe todos los datos y los guarda en cacao.csv
# ============================================================

import serial
import time
import sys

# -------- CONFIGURACION --------
PUERTO = 'COM14'        # <-- Cambiar al COM correcto si es otro
VELOCIDAD = 115200
ARCHIVO_SALIDA = 'cacao.csv'
TIMEOUT_SEGUNDOS = 120  # Maximo tiempo de espera (2 minutos)
# -------------------------------

print("=" * 50)
print("  DESCARGA DE DATOS - TESIS CACAO")
print("=" * 50)
print(f"\nConectando al ESP32 en {PUERTO}...")

try:
    ser = serial.Serial(PUERTO, VELOCIDAD, timeout=2)
    time.sleep(2)  # Espera estabilizacion
    print("Conexion establecida.")
except serial.SerialException as e:
    print(f"\nERROR: No se pudo abrir {PUERTO}")
    print("Verificar:")
    print("  1. Que el ESP32 este conectado")
    print("  2. Que el COM sea el correcto")
    print("  3. Que el Serial Monitor de Arduino este CERRADO")
    sys.exit(1)

# Limpiar buffer previo
ser.reset_input_buffer()

print("Enviando comando DUMP...")
ser.write(b'DUMP\n')

# Capturar datos
print("Recibiendo datos...\n")
capturando = False
lineas_capturadas = 0
inicio = time.time()

with open(ARCHIVO_SALIDA, 'w', encoding='utf-8', newline='') as f:
    while time.time() - inicio < TIMEOUT_SEGUNDOS:
        try:
            linea = ser.readline().decode('utf-8', errors='ignore').strip()
        except:
            continue
        
        if not linea:
            continue
        
        # Detectar inicio del dump
        if 'INICIO DUMP CSV' in linea:
            capturando = True
            print(">>> Inicio del CSV detectado")
            continue
        
        # Detectar fin del dump
        if 'FIN DUMP CSV' in linea:
            print(">>> Fin del CSV detectado")
            break
        
        # Capturar lineas de datos (deben tener comas)
        if capturando and ',' in linea:
            f.write(linea + '\n')
            lineas_capturadas += 1
            
            # Mostrar progreso cada 100 lineas
            if lineas_capturadas % 100 == 0:
                print(f"  Recibidas {lineas_capturadas} lineas...")

ser.close()

print("\n" + "=" * 50)
print(f"COMPLETADO")
print("=" * 50)
print(f"Archivo guardado: {ARCHIVO_SALIDA}")
print(f"Total de registros: {lineas_capturadas - 1}  (sin contar encabezado)")
print(f"\nAbrir el archivo {ARCHIVO_SALIDA} con Excel.")
print("Si las columnas no se separan: Datos -> Texto en columnas -> Coma")