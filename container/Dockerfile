# Dockerfile, Image, Container
FROM python:latest

WORKDIR /fastapi

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./API ./API

CMD ["python3", "./API/api.py"]