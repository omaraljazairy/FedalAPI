FROM python:3.8

# Update OS and install common dev tools
RUN apt-get update
RUN apt-get install -y wget vim git zip unzip less

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir /fedalapi
RUN mkdir /fedalapi/static
#working directory
WORKDIR /fedalapi

# execute the pip install upgrade first
RUN pip install --upgrade pip

# copy requirements.txt to the current working directory
COPY ./requirements.txt .

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /fedalapi
COPY . .