FROM python:3.11-slim-buster

RUN mkdir /api-peliculas
WORKDIR /api-peliculas

RUN apt-get update
RUN apt-get install -y curl

COPY . /api-peliculas/
RUN apt-get update && apt-get install -y postgresql-client
RUN apt-get install -y libpq-dev gcc
RUN pip3 install -r /api-peliculas/requirements.txt

ENV FLASK_APP="entrypoint:app"
ENV FLASK_ENV="development"
ENV APP_SETTINGS_MODULE="config.default"
ENV PORT 5000

EXPOSE ${PORT}
CMD ["flask", "run", "--host", "0.0.0.0"]

