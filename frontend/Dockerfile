FROM node:16

WORKDIR /app

# Install Vite globally
RUN npm install -g vite

# Copy package.json and package-lock.json first
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all other files
COPY . .

# Expose Vite default port
EXPOSE 8000

# Command to run the app
CMD ["npm", "run", "dev"]