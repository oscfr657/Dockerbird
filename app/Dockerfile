# pull official base image
FROM python:3.9.6-slim

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

# copy project
COPY . $APP_HOME

# Update & upgrade image
RUN apt update -y && apt upgrade -y

# install dependencies
RUN apt install git libmagic-dev -y

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache -r requirements.txt

# create the app user
RUN useradd -d /home/app app

# change to the app user
USER app
