# FROM python:3.11-slim

# ENV PYTHONUNBUFFERED=1 \
#     POETRY_VERSION=1.7.1

# WORKDIR /app

# COPY pyproject.toml poetry.lock ./

# RUN pip install "poetry==$POETRY_VERSION"

# RUN poetry install --no-dev

# COPY fastapi_poetry_template/ .

# CMD ["poetry", "run", "python", "server.py"]
