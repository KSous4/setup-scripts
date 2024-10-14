FROM python:3.12

RUN apt-get update && apt-get install -y postgresql postgresql-client libpq-dev

COPY . /setup

WORKDIR /setup

RUN pip install -r /setup/requirements.txt

CMD ["python3", "main.py"]
