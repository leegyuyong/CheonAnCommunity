FROM python:3.8

RUN apt-get update
WORKDIR /app
ADD requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app