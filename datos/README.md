# Datos del ensayo complementario

Este directorio contiene los registros obtenidos durante el ensayo complementario de captura de datos realizado en Santo Domingo de los Tsáchilas.

## Aclaración importante

El ensayo aquí documentado **no forma parte del alcance del Trabajo de Integración Curricular**. Se ejecutó como mecanismo auxiliar para alimentar el modo Real del HMI con un perfil térmico realista y evaluar el comportamiento del componente ante registros con dinámica natural. La arquitectura empleada para la captura no replica los sensores ni el hardware LoRa propuestos en el diseño del sistema.

## Contenido

- `ensayo_santo_domingo/fermentacion_para_nodero.csv`: registros del proceso.
- `ensayo_santo_domingo/metadatos.md`: descripción del ensayo.
- `ensayo_santo_domingo/extractor_serial.py`: script Python para extraer los datos desde el ESP32 vía puerto serial.

## Uso del CSV en el HMI

1. Copiar el archivo `fermentacion_para_nodero.csv` a la carpeta configurada en Node-RED, típicamente `C:\NodeRED-data\`.
2. Ingresar al HMI seleccionando el modo Real en la pantalla de Login.
3. El sistema cargará los registros y avanzará seis muestras por ciclo, reproduciendo el ensayo completo en aproximadamente 10 minutos.
