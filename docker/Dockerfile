FROM python:3.9.5

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN apt-get -y update && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt