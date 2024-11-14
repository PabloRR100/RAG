# Stage 1: Build stage
# FROM python:3.11-slim AS builder
FROM python:3.11 AS builder

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install dependencies needed for building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv in the build stage
RUN pip install --no-cache-dir uv

# Set the working directory
WORKDIR /app

# Copy only the necessary files for dependency installation
COPY pyproject.toml uv.lock /app/

# Create an isolated environment with uv and install dependencies
RUN uv sync --frozen

# Copy the application code into the build container
COPY src ./src

# Stage 2: Runtime stage
FROM python:3.11-slim

# Copy only the necessary files from the build stage
COPY --from=builder /app /app

# Set the working directory to /app
WORKDIR /app

# Set environment variables
ENV PYTHONPATH=/app/src

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]