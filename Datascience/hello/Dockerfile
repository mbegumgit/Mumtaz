# Dockerfile

# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code
ADD . /code
# Install dependencies
# runs the pip install command for all packages listed in the requirements.txt file
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

EXPOSE 8000