# Docker-101

## Instalando Docker

- [Docker Engine](https://docs.docker.com/engine/install/)

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
```