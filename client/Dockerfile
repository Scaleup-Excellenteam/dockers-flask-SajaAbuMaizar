# Assign the local Python version as a parent image
FROM python:3.7.4-alpine

# Set the main directory in the container and copy the current directory contents into the container
WORKDIR /app
COPY . /app

# Install the packages that are written in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 6000 available
EXPOSE 6000

# Run the program
CMD ["python", "client.py"]