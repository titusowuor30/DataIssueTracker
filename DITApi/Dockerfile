# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV DB_HOST=192.168.211.10
ENV DB_PORT=5432
ENV DB_NAME=dqits
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE DITApi.settings

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000

# Define the command to run your application
CMD ["gunicorn", "DITApi.wsgi:application", "--bind", "0.0.0.0:8000"]
