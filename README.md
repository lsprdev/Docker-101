# Docker-101

## Instalando Docker

- [Docker Engine](https://docs.docker.com/engine/install/)

## O que é o Docker?

Docker é uma plataforma que permite criar, implantar e gerenciar aplicações em containers. Containers são pacotes leves e portáteis que incluem tudo o que é necessário para executar uma aplicação: código, bibliotecas, dependências e configurações. Isso garante que a aplicação funcione de maneira consistente em diferentes ambientes, desde o desenvolvimento até a produção.

Além disso, Docker utiliza o conceito de imagens. Uma imagem Docker é um modelo imutável que contém o sistema de arquivos completo necessário para rodar uma aplicação, incluindo o código, bibliotecas e outras dependências. A partir de uma única imagem Docker, é possível criar múltiplos containers, que são instâncias em execução dessa imagem. Isso permite que a aplicação seja replicada facilmente e executada de forma isolada e consistente em qualquer ambiente.

#### Benefícios do Docker:

- **Portabilidade:** Containers podem ser executados em qualquer sistema que suporte Docker, garantindo consistência entre ambientes.

- **Isolamento:** Cada container é isolado do sistema host e de outros containers, aumentando a segurança e a estabilidade.

- **Eficiência:** Containers compartilham o kernel do sistema operacional, o que os torna mais leves e rápidos para iniciar em comparação com máquinas virtuais.

#### Repositórios de Imagens

As imagens Docker são armazenadas em repositórios, que podem ser públicos ou privados. O [Docker Hub](https://hub.docker.com/explore) é o repositório público padrão onde você pode encontrar milhares de imagens compartilhadas pela comunidade Docker. Pense no Docker Hub como se fosse um Github de Docker Images.

## Comandos Básicos

```bash
# Mostrando a versão do Docker
gabriel@lspr:~$ docker --version

# Rodando um container
gabriel@lspr:~$ docker run hello-world

# Baixando uma imagem
gabriel@lspr:~$ docker pull ubuntu

# Listando imagens
gabriel@lspr:~$ docker images ls

# Listando containers
gabriel@lspr:~$ docker ps # ou docker ps -a para mostrar todos os containers(até mesmo os que estão parados)

# Para listar todos os containers (incluindo os parados)
gabriel@lspr:~$ docker ps -a
```

## O que é o Dockerfile?

Um Dockerfile é um script de texto simples que contém um conjunto de instruções para construir uma imagem Docker. Cada instrução no Dockerfile cria uma camada na imagem, e quando você executa o Dockerfile, ele gera uma imagem que pode ser usada para criar containers.

#### Principais Instruções do Dockerfile:

- **FROM:** Define a imagem base a partir da qual a nova imagem será construída.

- **RUN:** Executa comandos no shell dentro do container.

- **COPY:** Copia arquivos ou diretórios do host para o sistema de arquivos do container.

- **CMD:** Especifica o comando que será executado quando um container é iniciado a partir da imagem.

- **EXPOSE:** Informa ao Docker que a aplicação no container escuta em portas específicas.

#### Exemplo de um Dockerfile Simples:

```dockerfle
# Usando uma imagem base oficial do Node.js
FROM node:14

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instalando dependências
RUN npm install

# Copiando o restante do código da aplicação
COPY . .

# Expondo a porta em que a aplicação será executada
EXPOSE 3000

# Definindo o comando para rodar a aplicação
CMD ["node", "app.js"]
```

#### O que é o Docker Compose?

Docker Compose é uma ferramenta que permite definir e gerenciar multi-containers Docker applications. Com o Docker Compose, você pode usar um arquivo YAML para configurar os serviços da sua aplicação, e depois iniciar todos eles com um único comando.

#### Principais Componentes do Docker Compose:

- **services:** Define os serviços que compõem a sua aplicação. Cada serviço é executado em um container separado.

- **volumes:** Permite que você monte diretórios do host dentro dos containers para persistência de dados.

- **networks:** Define redes customizadas para permitir a comunicação entre containers.

#### Exemplo de um Arquivo docker-compose.yml:

```yaml
version: '3'
services:
  web:
    image: my-web-app:latest
    build: .
    ports:
      - "80:80"
    volumes:
      - .:/app
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

#### Usando o Docker Compose:

- Usando o Docker Compose:
Iniciar serviços definidos no docker-compose.yml:

```bash
gabriel@lspr:~$ docker-compose up
```

- Parar serviços:

```bash
gabriel@lspr:~$ docker-compose down
```

## Docker Compose que Será Utilizado no Projeto

```yaml
version: '3.8'

services:
  backend:
    image: backend:latest
    build:
      context: ./backend
      dockerfile: Dockerfile
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    networks:
      - app-network

  frontend:
    image: frontend:latest
    build:
      context: ./frontend
      dockerfile: Dockerfile
    volumes:
      - ./frontend:/app
    ports:
      - "3000:3000"
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
```

### Explicando o docker-compose.yml

- **version:** Define a versão do Docker Compose que está sendo usada.

- **services:** Define os serviços que compõem a aplicação. Neste caso, temos dois serviços: backend e frontend.

- **backend:** e **frontend:** Define as configurações do serviço backend e frontend. Isso inclui a imagem a ser usada, o Dockerfile a ser usado para construir a imagem, os volumes a serem montados, as portas a serem expostas e a rede a ser usada.

- **volume:** Define os volumes a serem montados pelos serviços. Neste caso, estamos montando o diretório do host no diretório de trabalho do container.

- **ports:** Define as portas a serem expostas pelos serviços. Neste caso, estamos expondo a porta 8000 para o backend e a porta 3000 para o frontend.

- **networks:** Define as redes a serem usadas pelos serviços. Neste caso, temos uma rede chamada app-network.

## Referências

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Compose File Reference](https://docs.docker.com/compose/compose-file/)

