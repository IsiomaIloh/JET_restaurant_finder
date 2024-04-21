# Use an official Python runtime as a parent image
FROM python:3.12-slim-bullseye

ENV POETRY_VERSION=1.8.2

 # Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE = 1

# Prevents Python from buffering stdout and stderr to situations where
# the application crashes without emitting any logs due to the buffering.
ENV PYTHONUNBUFFERED = 1

# Set the working directory in the container to /app
WORKDIR usr/app

# Add the current directory contents into the container at /app
ADD . /app

# Install Poetry
RUN pip install poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock /usr/app/

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the application when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]