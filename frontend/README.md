## Dockerfile do Frontend:

#### O Dockerfile do frontend é responsável por criar a imagem do frontend da aplicação, para isso é necessário instalar as dependências do projeto e copiar o código fonte para a imagem.

```dockerfile
FROM node:16

WORKDIR /app

RUN npm install -g vite

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
```

#### Copie o conteúdo acima para um arquivo chamado `Dockerfile` na raiz do projeto frontend.

#### Para construir a imagem do frontend, execute o comando abaixo:

```bash
docker build -t frontend .
```