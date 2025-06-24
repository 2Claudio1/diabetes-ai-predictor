FROM node:20-alpine

# Directorio de trabajo
WORKDIR /app

# Copiamos e instalamos dependencias
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Copiamos la app
COPY . .

# Exponemos el puerto para Vite
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
