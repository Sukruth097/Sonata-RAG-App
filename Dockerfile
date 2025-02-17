# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure the main.py file exists in the /app directory
# RUN ls /app/main.py

# Expose the port the app runs on
EXPOSE 8087

# Define the command to run the application
CMD ["python", "src/main.py"]