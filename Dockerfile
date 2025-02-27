# Use official Python image
FROM python:3.9

# Set underlying shell
SHELL ["/bin/bash", "-c"]

# Set the working directory
WORKDIR /app

# Copy the application files
COPY requirements.txt .
COPY kafka_producer.py .
COPY kafka_consumer.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command (this will be overridden in docker-compose)
CMD ["python", "kafka_producer.py"]
