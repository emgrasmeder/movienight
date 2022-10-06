FROM python:3.10-slim AS base

ENV POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.2.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1

ENV PATH="$POETRY_HOME/bin:$PATH"


FROM base AS builder
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /src
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-ansi --no-dev --no-interaction --no-root


FROM builder AS final

ENV PATH="/src/.venv/bin:$PATH"

WORKDIR /app
COPY --from=builder /src/.venv ./venv
COPY movie_night/ ./movie_night
COPY resources ./resources

CMD ["python", "movie_night/app.py"]
