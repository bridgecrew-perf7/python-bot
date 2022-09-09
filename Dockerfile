FROM python:3.10.6

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN apt-get -y update && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

CMD ["python", "src/app.py"]