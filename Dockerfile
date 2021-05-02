FROM python:3.8-buster

WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.4 \
    PYTHONPATH=/app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION" && poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock /app/
COPY ./django-url-shortener/* .
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
EXPOSE 8000
RUN poetry install
ENTRYPOINT ["/docker-entrypoint.sh"]