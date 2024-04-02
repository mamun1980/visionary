# Use a slim version of the Python image
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev

# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the Django app code into the container
COPY . /app


# Copy the entrypoint script
COPY entrypoint.sh /app/

# Grant execute permissions to the entrypoint script
RUN chmod +x /app/entrypoint.sh

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Set the entrypoint script as the container entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]