# Assign the local Python version as a parent image
FROM python:3.7.4-alpine

# Add Maintainer Info
LABEL maintainer="name@example.com"

# Set the main directory in the container and copy the current directory contents into the container
WORKDIR /app
COPY . /app

# Install OpenJDK
RUN apk add --no-cache openjdk8


# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5003 available
EXPOSE 5003

# Run the program
CMD ["python", "java-executer.py"]