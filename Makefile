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

mypy: ## Run mypy checks
	@echo 'Running mypy ...'
	@docker-compose run --rm api pipenv run tox -e mypy
	@echo 'Mypy run finished'

unit_tests: ## Run unit tests
	@echo 'Running unit tests ...'
	@docker-compose run --rm api pipenv run tox -e unit_tests
	@echo 'Unit tests run finished'

integration_tests: ## Run integration tests
	@echo 'Running integration tests ...'
	@docker-compose run --rm api pipenv run tox -e integration_tests
	@echo 'Integration tests run finished'

unit_test_coverage: ## Run coverage
	@echo 'Running coverage ...'
	@docker-compose run --rm api pipenv run tox -e unit_test_coverage
	@echo 'Coverage run finished'

integration_test_coverage: ## Run coverage
	@echo 'Running coverage ...'
	@docker-compose run --rm api pipenv run tox -e integration_coverage
	@echo 'Coverage run finished'
