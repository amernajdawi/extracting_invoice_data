FROM python:3.10.14-slim-bullseye

WORKDIR /app

# Consolidate environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    OLLAMA_URL=http://ollama:11434

# Install system dependencies and clean up in a single layer
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python3 -

# Copy dependency files and install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Copy application code
COPY . .

# Expose port and set command
EXPOSE 8501
CMD ["poetry", "run", "streamlit", "run", "invoice_app.py"]
