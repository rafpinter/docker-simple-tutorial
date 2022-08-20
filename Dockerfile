# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /my-tests

COPY . .

CMD ["python3", "test.py"]