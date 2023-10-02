### BACKEND PYTHON CREDITCARD (TESTE MAIS TODOS)
O objetivo desse repositório é realizar o teste em Python (Programador Backend) seguindo as diretivas do seguinte link: [Teste Prático](https://github.com/MaisTodos/backend-python-creditcard)

### TECNOLOGIAS UTILIZADAS
 - Docker + Docker Compose
 - Python 3.10.x
 - FastAPI + uvcorn
 - SqlAlchemy (ORM)
 - psycopg2-binary (conexão com Postgres)
 - alembic (para migrations)
 - python-decouple (variáveis de ambiente)
 - passlib (criptografia de senhas)
 - python-jose (pra trabalhar com JWT)
 - python-multipart (pra trabalhar com form de login)

A escolha de montar o ambiente de desenvolvimento utilizando Docker com Docker Compose foi por basicamente 2 motivo: O primeiro motivo é que o meu ambiente de desenvolvimento vai ser muito parecido com o de produção e o segundo motivo é que meus colegas de trabalho podem executar esse ambiente facilmente se estiverem em um ambiente linux/unix/mac caso tenham do `Docker` + `docker-compose` devidamente instalados.

A princípio, eu tinha optado por utilizar `pipenv` por ele já criar um `ambiente virtual`, mas por algum motivo que não consegui entender, os o `FastAPI` não estava subindo corretamente. Então optei por utilizar o bom e velho `pip` com o arquivo `requirements.txt`. Pensando mais a fundo, o próprio docker já separa as dependências de desenvolvimento com as globais do sistema operacional, então não precisaria de um virtualenv.

Com base no que estudei recentemente, como o teste pede para criar somente uma API (e não uma solução web fullstack completa), decidi optar pelo framework [FastAPI](https://fastapi.tiangolo.com/), pois se trata de uma solução simples, rápida e extremamente escalável caso necessário.

Também optei por utilizar um ORM, no caso [SqlAlchemy](https://www.sqlalchemy.org/) para evitar de escrever queries SQL na mão, isso vai resultar em um código mais limpo e de fácil manutenção, por se tratar de um código 100% Python.

A opção de escolher o JWT para realizar autenticação é pelo fato de ter uma implementação simples e extremamente segura.

### AMBIENTE DE DESENVOLVIMENTO
Na raiz do projeto você vai encontrar o arquivo `docker-compose.yml` e `Dockerfile` que são os responsáveis por criar toda estrutura necessária para o desenvolvimento desse projeto.

Executando container:
```bash
docker-compose up -d
```

Verificando status do container:
```bash
docker-compose ps
```


Acessando projeto no browser:
```
http://127.0.0.1:8000
```

Acessando terminal do container:
```bash
docker-compose exec -it app sh
```

Comando para reconstruir os containers em caso de erros ou modificações no Dockerfile:
```bash
docker-compose build --no-cache && docker-compose up --force-recreate -d
```

Caso queira parar o container, basta digitar o seguinte comando:
```bash
docker-compose down
```