# syntax=docker/dockerfile:1
FROM --platform=linux/amd64 python:3.9

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install marwan

ENTRYPOINT ["marwan"]