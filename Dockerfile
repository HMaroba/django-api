# # The first instruction is what image we want to base our container on
# # We Use an official Python runtime as a parent image
# FROM python:3.10

# # The enviroment variable ensures that the python output is set straight
# # to the terminal with out buffering it first
# ENV PYTHONUNBUFFERED 1

# # Set the working directory to /music_service
# WORKDIR /

# # Copy the current directory contents into the container at /music_service
# ADD . /

# # Install dependencies
# COPY requirements.txt /
# RUN pip install -r requirements.txt

# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /node_api

# Install dependencies
COPY requirements.txt /node_api//
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /node_api/