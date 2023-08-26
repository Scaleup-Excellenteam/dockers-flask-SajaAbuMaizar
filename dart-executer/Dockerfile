# Assign the local Python version as a parent image
FROM python:3.7.4-alpine

# Set the main directory in the container and copy the current directory contents into the container
WORKDIR /app
COPY . /app

# Install required packages
RUN apk add --no-cache bash curl gnupg

# Import the key
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --import

# Install Dart SDK
RUN curl https://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-linux-x64-release.zip -o dartsdk.zip
RUN unzip dartsdk.zip -d /usr/lib
RUN rm dartsdk.zip
ENV PATH $PATH:/usr/lib/dart-sdk/bin

# Install the packages that re written in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5003 available
EXPOSE 5003

# Run the program
CMD ["python", "dart-executer.py"]
