# Usa una imagen base adecuada para tu aplicación. Aquí se utiliza una imagen de Python 3.9.
FROM python:3.8.12

# Establece el directorio de trabajo en el contenedor.
WORKDIR /app

# Copia los archivos de requerimientos (requirements.txt) a la imagen.
COPY requirements.txt .

# Instala las dependencias de tu aplicación.
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu aplicación al directorio de trabajo en el contenedor.
COPY . .

# Expone el puerto en el que se ejecuta tu aplicación.
EXPOSE 8000

# Define el comando para ejecutar tu aplicación.
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
