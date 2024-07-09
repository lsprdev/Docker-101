FROM node:16

WORKDIR /app

RUN npm install -g vite

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]