# Dockerfile, Image, Container
FROM python:latest

ADD main.py .
ADD user_filter.py .

RUN pip install requests beautifulsoup4 pandas curl-cffi

CMD [ "python", "./main.py" ]