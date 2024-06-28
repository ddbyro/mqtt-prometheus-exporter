# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD ./src /app

# Install any needed packages specified in requirements.txt
run pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8088 available to the world outside this container
EXPOSE 8088

# Run gunicorn when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:8088", "mqtt_prometheus_exporter:app"]