#Python official image
FROM python:3.12-slim

# Working Dir
WORKDIR /app

# Install system dependencies
# RUN apt-get update && apt-get install -y netcat gcc
RUN apt-get update && apt-get install -y netcat-openbsd gcc


# Copy project file
COPY . .

# Copy project files
COPY pyproject.toml poetry.lock ./

# Install poetry
RUN pip install poetry

# Install dependencies
# RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi


# Expose port
EXPOSE 8000

# Startup command
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]