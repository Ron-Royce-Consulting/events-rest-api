FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip

RUN pip3 install -r /app/requirements.txt


COPY ./api /app/

EXPOSE 8080



CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]
