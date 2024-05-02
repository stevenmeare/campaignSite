# Use Python Image from Docker Hub.
FROM python:latest

# Set the environment.
ENV PYTHONUNBUFFERED 1

# Set the working directory.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on.
EXPOSE 80

# Run the server and specify the port.
<<<<<<< HEAD
CMD ["python", "manage.py", "runserver", "localhost:8000"]
=======
CMD ["python", "manage.py", "runserver", "localhost:80"]
>>>>>>> campaignSite/master
