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
 - pytest (para testes unitários e de integração)
 - pydantic (para validação de dados em models)
 - cryptography (para guardar número de cartões criptografados)

A escolha de montar o ambiente de desenvolvimento utilizando Docker com Docker Compose foi por basicamente 2 motivo: O primeiro motivo é que o meu ambiente de desenvolvimento vai ser muito parecido com o de produção e o segundo motivo é que meus colegas de trabalho podem executar esse ambiente facilmente se estiverem em um ambiente linux/unix/mac caso tenham do `Docker` + `docker-compose` devidamente instalados.

A princípio, eu tinha optado por utilizar `pipenv` por ele já criar um `ambiente virtual`, mas por algum motivo que não consegui entender, os o `FastAPI` não estava subindo corretamente. Então optei por utilizar o bom e velho `pip` com o arquivo `requirements.txt`. Pensando mais a fundo, o próprio docker já separa as dependências de desenvolvimento com as globais do sistema operacional, então não precisaria de um virtualenv.

Com base no que estudei recentemente, como o teste pede para criar somente uma API (e não uma solução web fullstack completa), decidi optar pelo framework [FastAPI](https://fastapi.tiangolo.com/), pois se trata de uma solução simples, rápida e extremamente escalável caso necessário.

Também optei por utilizar um ORM, no caso [SqlAlchemy](https://www.sqlalchemy.org/) para evitar de escrever queries SQL na mão, isso vai resultar em um código mais limpo e de fácil manutenção, por se tratar de um código 100% Python.

A opção de escolher o JWT para realizar autenticação é pelo fato de ter uma implementação simples e extremamente segura.

---

### PASSOS RÁPIDOS PARA AMBIENTAÇÃO
1. Clone o projeto
2. Faça uma cópia do arquivo `.env.example` para `.env`
3. Com `docker` e `docker-compose` devidamente instalados, execute o comando:
```bash
docker-compose build --no-cache && docker-compose up --force-recreate -d
```
4. Rode as migrations para popular as tabelas no banco de dados com o seguinte comando:
```bash
docker-compose exec app alembic upgrade head
```
5. Acesse a documentação da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 
6. Divirta-se!

---

### DETALHES DO AMBIENTE DE DESENVOLVIMENTO
Na raiz do projeto você vai encontrar o arquivo `docker-compose.yml` e `Dockerfile` que são os responsáveis por criar toda estrutura necessária para o desenvolvimento desse projeto.
Antes de iniciar o projeto, faça uma cópia do arquivo `.env.example` para `.env` e gere sua criptografia HS256.

Gerando criptografia para adicionar em `SECRET_KEY` do `.env`:
```
1. Acesse https://www.browserling.com/tools/random-hex
2. Configure para 64 dígitos e 1 resultado
3. Clique em Generate Hex
4. Copie o resultado na chave SECRET_KEY

OBS: Caso queira gerar via linha de comando, basta digitar:
$ openssl rand -hex 64

ATENÇÃO: Pra fim de testes rápido para validar o funcionamento do projeto, eu já deixei meu .env no .env.example, mas uma aplicação real, eu iria remover dados sensíveis.
```

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

Acessando a documentação da API:
```
http://127.0.0.1:8000/docs
```

Acessando detalhes técnicos da API:
```
http://127.0.0.1:8000/redoc
```

`Atenção:` Caso queira utilizar o postman como RESTClient deixei todas as collection que utilizei em `docs/postman-collection`

Acessando o PgAdmin (gestão do banco postgresql):
Caso queira acessar o `pgadmin4`, basta parar seus containers, acessar o arquivo `docker-compose.yml`, remover os comentários, subir os containers novamente.
```
http://127.0.0.1:5050
user: admin@admin.com
pass: password

Para conectar no serviço 'database' do docker, utilize o seguinte IP:
host.docker.internal
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

Para executar os testes, basta digitar o seguinte comando:
```bash
docker-compose exec app pytest
```

Para criar novos arquivos de migração (migration), execute o seguinte comando:
```bash
# Autogeração:
docker-compose exec app alembic revision --autogenerate -m "migration name"

# Criação manual: 
docker-compose exec app alembic revision -m "migration name"

# Exemplos usado nesse projeto:
docker-compose exec app alembic revision --autogenerate -m "add users table"
docker-compose exec app alembic revision -m "add credit_cards table"
```

Para aplicar uma migração (criar de fato no banco de dados), execute o seguinte comando:
```bash
docker-compose exec app alembic upgrade head
```
Atenção: Esse comando é obrigatório sempre que baixar o repo em um novo computador, reconstruir seus containers ou caso tenha algum erro 500 na API.

### USO DA API
Usuários não podem ser e-mails, ou seja, não pode conter @:
```
icarowilliam2023 # correto
icaro@teste.com # errado
```

Não é possível registrar 2 usuários com mesmo nome, pois vamos obter o seguinte erro:
```
User already exists
```

### PROBLEMAS A SEREM RESOLVIDOS (ISSUES)
1. Não sei por qual motivo o endpoint `/v1/credit-cards` (em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)) não está conseguindo colocar o Bearer Token no cabeçalho para enviar as requisições. Ele deixa o token como "undefined". Exemplo:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/credit-cards' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer undefined'
```
Se testar a API em um REST-Client (Postman, Insomnia, etc) funciona normalmente, bastando cadastrar o usuário, fazer o login e, em seguida, consumir o endpoint `[GET] /v1/credit-cards`

2. Nos erros de validação eu gostaria muito de utilizar o `ValidationError` do `pydantic`, mas por algum motivo (que não tenho conhecimento no momento), exibe um erro de contrutor. Tentei mudar o decorator para `@staticmethod` e também remove-lo e não funcionou. Pra não interromper o projeto, eu troque a exception de `ValidationError` para `HTTPException` do `fastapi`.
3. A minha intenção exibir os cartões no padrão `*******1234`, onde `1234` era os 4 últimos dígitos do cartão. Mas não tive tempo pra finalizar essa implementação (faltou um pouco mais de estudo na forma de como guardar e retornar binários no postgres)
4. Eu queria ter mais tempo pra criar mais testes unitários para algumas funcionalidades (tipo testar todas as funções do `custom_helpers`, etc).