FROM python:3.11

# Set the environment variable
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.7.1

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry install $(test "$ENVIRONMENT" == production && echo "--only=main") --no-interaction --no-ansi

# Creating folders, and files for a project:
RUN apt-get update && apt-get install -y libsndfile1


COPY . /code

CMD ["bash", "process_audio.sh"]
