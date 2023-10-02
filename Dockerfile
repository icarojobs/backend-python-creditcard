FROM python:3.11-alpine

WORKDIR /home/python/app

COPY ./requirements.txt /home/python/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/python/app/requirements.txt

COPY . /home/python/app