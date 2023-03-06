FROM python:3.8.14-slim

ARG development
ENV DEVELOPMENT $development

ENV PYTHONPATH "${PYTHONPATH}:/srv:/srv/src"

COPY . /srv/

WORKDIR /srv

RUN pip install pipenv \
    && pipenv lock \
    && pipenv install --system --deploy \
    && adduser -u 1000 --gecos "" --disabled-password deng \
    && mkdir /venv \
    && chown -R deng:deng /venv \
    && chown -R deng:deng /srv

EXPOSE ${DDD_EDD_PRACTICE_API_PORT}

CMD ["uvicorn", "app.ddd_edd_practice_app:app", "--host=0.0.0.0", "--port=5000"]
