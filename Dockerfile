FROM python:3.9.5

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD python src/app.py