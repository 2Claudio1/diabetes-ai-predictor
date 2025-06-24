FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos la app
COPY . .

# Exponemos el puerto y lanzamos uvicorn para FastAPI
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
