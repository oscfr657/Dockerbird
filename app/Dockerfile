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

# copy project
COPY . $APP_HOME

# install dependencies
RUN apt update -y
RUN apt install git memcached libmagic-dev -y

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache -r requirements.txt


# create the app user
RUN useradd -d /home/app app

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app
