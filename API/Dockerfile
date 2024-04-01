# Use an official Python runtime as a parent image
FROM python:3.10-slim

LABEL maintainer="Docker student"\
        description="This is a data loader for the API to get data from an API and store it in memory"

# Set the working directory in the container to /app
WORKDIR /app

# define environment variables
# ensures that the python output is sent to the terminal without buffering
ENV PYTHONUNBUFFERED=TRUE

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN  pip --no-cache-dir install --upgrade pip &&\
            pip --no-cache-dir install --requirement requirements.txt

# Specifies the storage location to be the directory app
# therefore, files generated will be stored there as an example
# Create mountpoint
VOLUME /app

# Run app.py when the container launches
CMD ["python", "app.py"]