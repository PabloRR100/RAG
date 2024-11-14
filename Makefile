# Variables
APP_NAME=rag-api
PYPROJECT=pyproject.toml

SRC_DIR=src
API_DOCKERFILE_PATH=src/api/Dockerfile

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

# Lint Python files
.PHONY: lint
lint:
	@echo "Running linter..."
	uv exec -- flake8 $(SRC_DIR)

# Format code with Black
.PHONY: format
format:
	@echo "Formatting code with Black..."
	uv exec -- black $(SRC_DIR)

# Run tests (adjust command as needed)
.PHONY: test
test:
	@echo "Running tests..."
	uv exec -- pytest $(SRC_DIR)


# ---
# API targets
# ---

# Build the Docker image
.PHONY: build-api
build-api:
	@echo "Building Docker image..."
	docker build -t $(APP_NAME) -f $(API_DOCKERFILE_PATH) .

# Run the Docker container
.PHONY: run-api
run-api:
	@echo "Running Docker container..."
	docker run -p 8000:8000 --name $(APP_NAME) $(APP_NAME)

# Stop the Docker container
.PHONY: stop
stop:
	@echo "Stopping Docker container..."
	docker stop $(APP_NAME) || true
	docker rm $(APP_NAME) || true

# Clean up Docker images and containers
.PHONY: clean
clean: stop
	@echo "Cleaning up Docker images and containers..."
	docker rmi $(APP_NAME) || true
	docker container prune -f
	docker image prune -f