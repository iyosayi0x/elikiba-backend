FROM ubuntu:20.04
FROM python:3.11

ENV TZ="US"

# Set timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install necessary packages
RUN apt-get update 
RUN apt-get install -y postgresql-client

# Set up the working directory
RUN mkdir -p /usr/app
WORKDIR /usr/app

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# copy whole project to your docker home directory. 
COPY . /usr/app/

# remove default nginx conf 
RUN echo "Deleting default nginx conf"
RUN rm -fr /etc/nginx/conf.d/default.conf

# copy requirements
COPY ./requirements.txt /usr/app/requirements.txt

# upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get install -y vim 