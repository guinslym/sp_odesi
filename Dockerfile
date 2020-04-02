# Use an official Python runtime as an image
FROM ubuntu:18.04

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY . /app

ENV DATABASE mysql

COPY scripts/docker/install-python.bash /app
RUN /install-python.bash

RUN apt-get install -qq --no-install-recommends \
    curl \
    coreutils \
    openssl \
    findutils \
    sed \
    default-mysql-client-core && \
    apt-get autoclean \
    > /dev/null

RUN pip install poetry
RUN pip install -r requirements.txt 
RUN python odesi_tables.py
