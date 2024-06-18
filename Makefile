SERVICE_NAME ?= placeholder

.PHONY: init

init:
	@echo "Initializing project with name: $(SERVICE_NAME)"
	# Replace project name in all text files (excluding binary files and the Makefile)
	@find . -type f ! -name "*.bin" ! -name "Makefile" -exec grep -Iq . {} \; -and -exec sed -i '' -e "s/fastapi_poetry_template/$(SERVICE_NAME)/g" {} +
	# Rename the root directory if needed (assume root directory name is fastapi_poetry_template)
	@if [ -d fastapi_poetry_template ]; then mv fastapi_poetry_template $(SERVICE_NAME); fi
	# Replace package name in pyproject.toml (or any other files referencing the old name)
	@sed -i '' -e "s/^name = \"fastapi-poetry-template\"/name = \"$(SERVICE_NAME)\"/g" pyproject.toml
	@sed -i '' -e "s/fastapi_poetry_template/$(SERVICE_NAME)/g" pyproject.toml
	@echo "Project initialized with name: $(SERVICE_NAME)"
	# Setup virtual environment and install dependencies using Poetry
	@python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip install poetry && \
	poetry install
