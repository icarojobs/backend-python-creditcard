FROM python:3.11-alpine

WORKDIR /home/python/app

RUN apk update && apk add git
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo

COPY ./requirements.txt /home/python/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/python/app/requirements.txt
RUN pip install git+https://github.com/maistodos/python-creditcard.git@main

COPY . /home/python/app