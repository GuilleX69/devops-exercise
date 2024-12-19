# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of post-service directory into the container
COPY . /app

# Install Flask
RUN pip install flask

# Expose port 5000 for the post-service
EXPOSE 5000

# Define environment variable for the Flask app
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["python", "app.py"]
