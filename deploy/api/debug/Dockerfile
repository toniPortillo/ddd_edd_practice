FROM python:3.8.14-slim

ARG development
ENV DEVELOPMENT $development

ENV PYTHONPATH "${PYTHONPATH}:/srv:/srv/src"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /srv/

WORKDIR /srv

RUN pip install pipenv \
    && pipenv lock \
    && pipenv install --system --deploy

RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
    chown -R appuser /srv

USER appuser

EXPOSE ${DDD_EDD_PRACTICE_API_PORT}
