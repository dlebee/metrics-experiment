# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY app.py .

# Install Flask, which is used to serve the metrics
RUN pip install flask prometheus_client

# Expose the port
EXPOSE 8000

# Run the Python script
CMD ["python", "app.py"]