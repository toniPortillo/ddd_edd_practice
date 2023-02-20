FROM python:3.8.14-slim

ARG development
ENV DEVELOPMENT $development

ENV PYTHONPATH "${PYTHONPATH}:/srv:/srv/src"

COPY . /srv/

WORKDIR /srv/deploy/api/docker

WORKDIR /srv

RUN pip install pipenv

EXPOSE ${DDD_EDD_PRACTICE_API_PORT}

CMD ["uvicorn", "srv.main:app", "--host:0.0.0.0", "--port=5000"]
