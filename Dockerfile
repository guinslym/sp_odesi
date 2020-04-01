# Use an official Python runtime as an image
FROM ubuntu

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY . /app
RUN pip install poetry
RUN pip install -r requirements.txt 
