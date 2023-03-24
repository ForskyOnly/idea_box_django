FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1 

ENV SECRET_KEY=d36vzj54#1=#-m7*r+1n#gvq%g3w-g^i@820ckeohmwy1

ENV  DEBUG=1

COPY . /app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]