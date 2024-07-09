## Dockerfile do Backend:

#### O Dockerfile do backend é responsável por criar a imagem do backend da aplicação, para isso é necessário instalar as dependências do projeto e copiar o código fonte para a imagem.

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### Copie o conteúdo acima para um arquivo chamado `Dockerfile` na raiz do projeto backend.

#### Para construir a imagem do backend, execute o comando abaixo:

```bash
docker build -t backend .
```