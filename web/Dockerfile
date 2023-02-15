# pull official base image
FROM python:slim
# create directory for the web user
RUN mkdir -p /home/web
# create the appropriate directories
ENV HOME=/home/web
RUN mkdir $HOME/static
RUN mkdir $HOME/media
WORKDIR $HOME
# create the web user
RUN useradd -d /home/web -m web
# set environment variables
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER 1
# copy project
COPY --chown=web:web ./web $HOME
# Update & upgrade image
RUN apt update -y && apt upgrade -y
# install dependencies
RUN apt install git libmagic-dev -y
# install python dependencies
RUN python -m pip install --upgrade pip
COPY ./web/requirements.txt .
RUN pip install --no-cache -r requirements.txt
# chown all the files to the web user
RUN chown web:web -R $HOME
# change to the web user
USER web