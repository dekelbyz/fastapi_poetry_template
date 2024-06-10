FROM python:3.11-bullseye

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    PYTHONPATH=/app

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install "poetry==1.8.*" && \
    poetry config virtualenvs.create false  && \
    poetry lock --check && \
    poetry install --no-interaction --no-ansi --no-root

COPY . ./

RUN poetry install --no-interaction --no-ansi

EXPOSE 6000

# CMD ["sleep", "90000"]

ENTRYPOINT ["poetry", "run", "python3", "fastapi_poetry_template/server.py"]
