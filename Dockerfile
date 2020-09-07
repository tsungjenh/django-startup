FROM python:3.6.8
LABEL maintainer tsungjen
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_http
RUN mkdir -p /var/log/django_http/
RUN ls /home
RUN adduser ubuntu
WORKDIR /django_http
COPY . /django_http/
RUN ls .
RUN pip install -r requirements.txt