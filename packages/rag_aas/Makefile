# Variables
APP_NAME=rag_aas
PYPROJECT=pyproject.toml


# Default rule
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  install      - Install dependencies using uv"
	@echo "  build        - Build the Docker image"
	@echo "  run          - Run the Docker container"
	@echo "  stop         - Stop the Docker container"
	@echo "  clean        - Remove Docker image and stopped containers"

# Install dependencies using uv
.PHONY: install
install:
	@echo "Installing dependencies with uv..."
	uv install --no-project

.PHONY: ruff
ruff:
	@echo "Running ruff..."
	uv run ruff 

# Run tests (adjust command as needed)
.PHONY: test
test:
	@echo "Running tests..."
	uv exec -- pytest $(SRC_DIR)



# Build Package
.PHONY: build
build:
	uv build

