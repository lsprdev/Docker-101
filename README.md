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

# Para listar todos os containers (incluindo os parados)
gabriel@lspr:~$ docker ps -a
```

## O que são imagens no Docker?

No Docker, uma imagem é um pacote leve e independente que contém tudo o que é necessário para executar uma aplicação, incluindo o código, runtime, bibliotecas, variáveis de ambiente e configurações. As imagens são a base dos containers Docker. Quando você executa uma imagem, ela se transforma em um container.

### Características das Imagens Docker:

- **Leveza:** Imagens Docker são menores em tamanho, facilitando o download e a inicialização rápida.

- **Portabilidade:** Podem ser executadas em qualquer ambiente que tenha o Docker instalado.

- **Imutabilidade:** As imagens são somente leitura; qualquer mudança nelas cria uma nova camada, permitindo o controle de versões e histórico.

- **Reusabilidade:** Imagens podem ser reutilizadas para criar múltiplos containers idênticos.

