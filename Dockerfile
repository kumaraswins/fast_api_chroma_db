# Use the official Python base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file to the working directory

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY  ./app /code/app

# Expose the port on which the application will run
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
