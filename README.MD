### BACKEND PYTHON CREDITCARD (TESTE MAIS TODOS)
O objetivo desse repositório é realizar o teste em Python (Programador Backend) seguindo as diretivas do seguinte link: [Teste Prático](https://github.com/MaisTodos/backend-python-creditcard)

### TECNOLOGIAS UTILIZADAS
 - Docker + Docker Compose
 - Python 3.10.x
 - pipenv
 - FastAPI + uvcorn
 - SqlAlchemy (ORM)
 - psycopg2-binary (conexão com Postgres)
 - alembic (para migrations)
 - python-decouple (variáveis de ambiente)
 - passlib (criptografia de senhas)
 - python-jose (pra trabalhar com JWT)
 - python-multipart (pra trabalhar com form de login)

A escolha de montar o ambiente de desenvolvimento utilizando Docker com Docker Compose foi por basicamente 2 motivo: O primeiro motivo é que o meu ambiente de desenvolvimento vai ser muito parecido com o de produção e o segundo motivo é que meus colegas de trabalho podem executar esse ambiente facilmente se estiverem em um ambiente linux/unix/mac caso tenham do `Docker` + `docker-compose` devidamente instalados.

A opção de utilizar o `pipenv` ao invés do `pip` foi simplesmente pelo fato de se tratar de um gerenciados de dependências mais moderno, ou seja, não preciso criar um `requirements.txt` pra controlar minhas dependências e ainda já vou ter um ambiente virtual (virtualenv) prontinho pra ser utilizado.

Com base no que estudei recentemente, como o teste pede para criar somente uma API (e não uma solução web fullstack completa), decidi optar pelo framework [FastAPI](https://fastapi.tiangolo.com/), pois se trata de uma solução simples, rápida e extremamente escalável caso necessário.

Também optei por utilizar um ORM, no caso [SqlAlchemy](https://www.sqlalchemy.org/) para evitar de escrever queries SQL na mão, isso vai resultar em um código mais limpo e de fácil manutenção, por se tratar de um código 100% Python.

A opção de escolher o JWT para realizar autenticação é pelo fato de ter uma implementação simples e extremamente segura.

### AMBIENTE DE DESENVOLVIMENTO
Na raiz do projeto você vai encontrar o arquivo `docker-compose.yml` e o diretório `/docker` que são os responsáveis por criar toda estrutura necessária para o desenvolvimento desse projeto.

Acessando terminal do container:
```bash
docker-compose exec -it app sh
```

Instalando dependências do projeto (através do terminal do container)
```bash
pipenv install
```

Instalando dependências adicionais (através do terminal do container):
```bash
pipenv install nome-da-dependencia

# exemplo usado nesse projeto:

pipenv install fastapi uvicorn sqlalchemy psycopg2-binary alembic python-decouple passlib python-jose python-multipart
```

Ativando virtualenv:
```bash
pipenv shell
```