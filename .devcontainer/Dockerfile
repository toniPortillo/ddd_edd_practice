FROM python:3.8.14-slim

ARG development
ENV DEVELOPMENT $development

ENV PYTHONPATH "${PYTHONPATH}:/srv:/srv/src"

COPY . /srv/

WORKDIR /srv

RUN pip install pipenv \
    && pipenv lock \
    && pipenv install --system --deploy
