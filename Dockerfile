FROM python:3.6.5-slim

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y gcc make nano wget jq && \
    rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile

RUN ln -s /usr/local/bin/python /bin/python && \
    pip install pip setuptools --upgrade && \
    pip install pipenv && \
    pipenv install --deploy --system && \
    pipenv install --dev --deploy --system
