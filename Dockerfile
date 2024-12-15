# Python 3.7 image from Docker Hub
FROM python:3.7

# Setting working directory inside the container
WORKDIR /app

# Copying the application files to the container
COPY . /app

# Installing dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposing the port that the app will run on
EXPOSE 5000

# Command to run the app using Gunicorn with 4 workers
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "app:app"]
