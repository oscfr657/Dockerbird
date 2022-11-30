# pull official base image
FROM python:slim

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
RUN mkdir $HOME/static
RUN mkdir $HOME/media
WORKDIR $HOME

# set environment variables
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER 1

# copy project
COPY ./app $HOME

# Update & upgrade image
RUN apt update -y && apt upgrade -y

# install dependencies
RUN apt install git libmagic-dev -y

# install python dependencies
RUN python -m pip install --upgrade pip
COPY ./app/requirements.txt .
RUN pip install --no-cache -r requirements.txt

# create the app user
RUN useradd -d /home/app app

# chown all the files to the app user
RUN chown -R app:app $HOME

# change to the app user
USER app
