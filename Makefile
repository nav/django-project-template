SHELL := /bin/bash
.DEFAULT_GOAL := help

# Read and load environment variables from .env if it exists
ifneq (,$(wildcard ./.env))
	include .env
	export
endif

# When adding a phony target, add to the list below. These are namespaced by
# their scope.
.PHONY: help install run css test
.PHONY: run/docker
.PHONY: migrations migrate
.PHONY: static


DATABASE_HOST ?= 127.0.0.1
DATABASE_NAME ?= app
DATABASE_USER ?= app
DATABASE_PASSWORD ?= app


help:			## Show this help
	@printf "\nUsage: make <command>\n\nThe following commands are available:\n\n"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/ [a-z\/]*	//' | sed -e 's/##//'
	@printf "\n"

db_creds:
	@printf "[app_service]\nhost=${DATABASE_HOST}\nuser=${DATABASE_USER}\ndbname=${DATABASE_NAME}\nport=5432\n" > .pg_service.conf
	@printf "${DATABASE_HOST}:5432:*:${DATABASE_USER}:${DATABASE_PASSWORD}" > .pgpass
	@chmod 600 .pgpass

db: db_creds
	@./bin/install_db --recreate ${DATABASE_NAME}


install: run/docker			## Install dependencies and run docker services
	@uv sync
	@echo "Creating password for superuser"
	@uv run python src/manage.py createsuperuser --username=nav --email=nav@navaulakh.com
	@uv run python src/manage.py createtenant \
		--domain="localhost:8000" \
		--name=Localhost \
		--street="123 Main St" \
		--city=Surrey \
		--province='BC' \
		--country=CA \
		--postal_code="V3W 1S9" \
		--phone="604-555-1234" \
		--email="info@example.com" \
		--logo="./src/static/img/logo.png"


run:			## Run Django application server
	@uv run --no-sync gunicorn --config gunicorn-config.py project.wsgi

server:
	@uv run --no-sync python src/manage.py runserver 0.0.0.0:8000

css:			## Run tailwind CLI to render CSS
	@tailwindcss -i ./src/static/css/input.css -o ./src/static/css/output.css --watch

test:			## Run tests for the  project
	@uv run --no-sync pytest $(path)


##
##- Services -
run/docker:		## Run docker services
	@docker-compose up -d db cache objectstore &> /dev/null
	@sleep 5
##
##- Migrations -
migrations:		## Make new migrations
	@uv run --no-sync python src/manage.py makemigrations --no-input

migrate:		## Run migrations and update database
	@uv run --no-sync python src/manage.py migrate --no-input

##
##- Static -
static:			## Collect static files
	@uv run --no-sync python src/manage.py collectstatic --no-input
