### BACKEND PYTHON CREDITCARD (TESTE MAIS TODOS)
O objetivo desse repositório é realizar o teste em Python (Programador Backend) seguindo as diretivas do seguinte link: [Teste Prático](https://github.com/MaisTodos/backend-python-creditcard)

### TECNOLOGIAS UTILIZADAS
 - Docker + Docker Compose
 - Python 3.10.x
 - FastAPI + uvcorn
 - SqlAlchemy (ORM)

A escolha de montar o ambiente de desenvolvimento utilizando Docker com Docker Compose foi por basicamente 2 motivo: O primeiro motivo é que o meu ambiente de desenvolvimento vai ser muito parecido com o de produção e o segundo motivo é que meus colegas de trabalho podem executar esse ambiente facilmente se estiverem em um ambiente linux/unix/mac caso tenham do `Docker` + `docker-compose` devidamente instalados.

Com base no que estudei recentemente, como o teste pede para criar somente uma API (e não uma solução web fullstack completa), decidi optar pelo framework [FastAPI](https://fastapi.tiangolo.com/), pois se trata de uma solução simples, rápida e extremamente escalável caso necessário.

Também optei por utilizar um ORM, no caso [SqlAlchemy](https://www.sqlalchemy.org/) para evitar de escrever queries SQL na mão, isso vai resultar em um código mais limpo e de fácil manutenção, por se tratar de um código 100% Python.

