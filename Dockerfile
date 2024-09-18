FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

COPY ./migration/migration_up.sql /docker-entrypoint-initdb.d/

EXPOSE 3000

CMD ["python", "-m" ,"app.index"]