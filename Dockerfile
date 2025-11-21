FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . /app

RUN chmod +x entrypoint.sh

EXPOSE 3202
EXPOSE 3203
EXPOSE 3204
ENTRYPOINT ["./entrypoint.sh"]
