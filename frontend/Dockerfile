FROM node:20-alpine

# Crear directorio de trabajo
WORKDIR /app

# Copiar solo archivos necesarios para instalación
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar toda la app (incluye src/, tsconfig.json, shims, etc.)
COPY . .

# Compilar
RUN npm run build

# Exponer puerto de desarrollo (opcional si vas a usar solo producción)
EXPOSE 5173

# Comando por defecto: modo desarrollo (puedes cambiar a producción si deseas)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
