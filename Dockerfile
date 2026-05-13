FROM node:24-bookworm-slim AS node

FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:$PATH"

COPY --from=node /usr/local /usr/local
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev
COPY --chmod=755 docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

EXPOSE 2718

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
