# ```open-zqecg-parser``` 🩺🔓
### A Python-based utility to rescue and visualize ECG data from proprietary Zoncare ```.zqecg``` files.

### 📖 El Problema (The Why)
Muchos dispositivos médicos modernos, como los electrocardiógrafos de Zoncare, almacenan los estudios en formatos propietarios y binarios (```.zqecg```). Esto crea una barrera de "secuestro de datos" donde pacientes y médicos no pueden visualizar la información sin licencias costosas o software restrictivo que solo corre en Windows.

Este proyecto nace de una necesidad urgente: **devolverle al paciente la propiedad de sus propios datos biométricos.**

### 🚀 Características
- **Independencia de Plataforma:** Corre en cualquier sistema con Python (probado en Fedora Linux).

- **Extracción Directa:** Lee los archivos binarios crudos sin necesidad de licencias o "dongles".

- **Generación de PDF:** Crea reportes visuales con rejilla milimetrada para facilitar la lectura médica.

- **Transparencia:** Código abierto para que cualquiera pueda verificar cómo se interpretan los datos.

### 🛠️ Instalación y Requisitos
Necesitas tener instalado Python 3 y las librerías de procesamiento de datos:


```Bash
pip install numpy matplotlib
```

### 📋 Uso
1. Coloca tus archivos ```.zqecg``` en la misma carpeta que el script.

2. Ejecuta el convertidor:

```Bash
python3 convert_ecg.py
```

### 🧬 Detalles Técnicos
El script interpreta el formato binario de Zoncare (específicamente de modelos como la serie **iMAC**) realizando un bypass del encabezado de 128 bytes y separando los canales intercalados de 32 bits.

### ⚠️ Descargo de Responsabilidad (Medical Disclaimer)
**Este software es una herramienta de visualización técnica, no un dispositivo médico.**
La interpretación de un electrocardiograma debe ser realizada exclusivamente por un profesional de la salud (Cardiólogo). No utilices este script para autodiagnóstico. El autor no se hace responsable de decisiones médicas tomadas basadas en esta visualización.

### 🤝 Créditos y Origen
Este proyecto es fruto de una colaboración única entre un usuario de Linux comprometido con la libertad de datos y **Gemini** (la IA de Google).

- **Concepto y Pruebas:** Roberto Tavitas.

- **Desarrollo de Lógica:** Gemini 3 Flash.