#!/usr/bin/make -f

PROJECT_NAME := 'ddd_edd_practice'
.DEFAULT_GOAL := help
WHITELABEL_NAME := $(shell cat .env | grep SERVICE_NAME | cut -d '=' -f 2)

flake8: ## Run flake8 checks
	@echo 'Running flake8 ...'
	@docker-compose run --rm api pipenv run tox -e flake8
	@echo 'Flake 8 run finished'

black: ## Run black checks
	@echo 'Running black ...'
	@docker-compose run --rm api pipenv run tox -e black
	@echo 'Black run finished'
