FROM python:3.12-alpine
LABEL org.opencontainers.image.authors="nav@navaulakh.com"

ENV APP_USER=app_user
ARG ENVCONSUL_VERSION=0.13.2
ARG VAULT_VERSION=1.15.4

# Create and setup workdir
RUN mkdir -p /app
WORKDIR /app

# Install os dependencies
RUN apk add --no-cache \
        gcc \
        jpeg-dev \
        libffi-dev \
        libxslt-dev \
        musl-dev \
        python3-dev \
        zlib-dev \
        bash \
        curl \
        jq \
        postgresql-client \
        postgresql-dev \
        openssh-client \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        git \
        libxml2-dev \
        linux-headers \
        xmlsec-dev

# Trust github host
RUN mkdir $HOME/.ssh/ && touch $HOME/.ssh/known_hosts && ssh-keyscan github.com >> $HOME/.ssh/known_hosts

# Install Vault and Envconsul
RUN wget https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip \
    && unzip envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip -d /usr/local/bin \
    && rm envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip \
    && wget https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip \
    && unzip vault_${VAULT_VERSION}_linux_amd64.zip -d /usr/local/bin \
    && rm vault_${VAULT_VERSION}_linux_amd64.zip

# Create application user
RUN adduser --disabled-password --gecos '' $APP_USER

# Setup virtualenv and install dependencies
COPY pyproject.toml uv.lock ./

# uv
ENV UV_LINK_MODE=copy \
    UV_INSTALL_DIR=/usr/local \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.12 \
    UV_PROJECT_ENVIRONMENT=/app/.venv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh  && rm /uv-installer.sh

RUN chown -R ${APP_USER}:${APP_USER} /app
USER ${APP_USER}
RUN uv sync --frozen --no-dev --no-install-project && rm pyproject.toml uv.lock
