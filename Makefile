# Makefile

SERVICE_NAME ?= my_service

.PHONY: init

init:
	@echo "Initializing project with name: $(SERVICE_NAME)"
	# Replace project name in all files
	@find . -type f -exec sed -i '' "s/fastapi_poetry_template/$(SERVICE_NAME)/g" {} +
	# Rename the root directory if needed (assume root directory name is fastapi_poetry_template)
	@if [ -d fastapi_poetry_template ]; then mv fastapi_poetry_template $(SERVICE_NAME); fi
	# Replace package name in pyproject.toml (or any other files referencing the old name)
	@sed -i '' "s/fastapi_poetry_template/$(SERVICE_NAME)/g" pyproject.toml
	@echo "Project initialized with name: $(SERVICE_NAME)"
