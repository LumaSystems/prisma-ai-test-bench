# Base image with Python and dependencies
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y curl


# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip uv
RUN UV_HTTP_TIMEOUT=1000 uv pip install --system --no-cache -r  requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:${PWD}"

# Copy the project files
COPY . .

# Set the default command (This will be overridden by `docker-compose.yml`)
CMD ["python", "-m", "test_bench.text_generator"]
