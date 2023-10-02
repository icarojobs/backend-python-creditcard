# Optei por basear na imagem *-slim por ser bem leve
FROM python:3.10.2-slim

# Optei por usar pipenv por vários motivos
# 1. pra não ter minhas dependências globais em todos os projetos
# 2. pra ter um virtualenv
# 3. pra ter um manifesto/lock-file com versões das libs que vou utilizar
RUN pip install pipenv

# Criei um usuário novo (não root). A home será em /home/python
RUN useradd -ms /bin/bash python

# Aqui troco de usuário 'root' para usuário 'python'
USER python

# Aqui defino o diretório de trabalho dentro do container que estamos criando
WORKDIR /home/python/app

# Aqui já ativo o virtualenv dentro desse container/projeto
ENV PIPENV_VENV_IN_PROJECT=True

# Para manter o container em execução constante, executamos o comando abaixo
CMD ["tail", "-f", "/dev/null"]
