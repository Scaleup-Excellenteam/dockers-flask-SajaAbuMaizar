# Assign the local Python version as a parent image
FROM python:3.7.4-alpine

# Set the main directory in the container and copy the current directory contents into the container
WORKDIR /app
COPY . /app

# Install the packages that are written in the file requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5003 available
EXPOSE 5003

# Run the program
CMD ["python", "python-executer.py"]