# pull official base image
FROM python:3.12-slim
# create a web user
RUN useradd -m web
# create the appropriate directories
ENV HOME=/home/web
RUN mkdir $HOME/static
RUN mkdir $HOME/media
WORKDIR $HOME
# set environment variables
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
# copy project
COPY --chown=web:web ./web $HOME
COPY ./web/requirements.txt $HOME
# Update & upgrade image
RUN apt update -y && apt upgrade -y
# install dependencies
RUN apt install -y git libmagic-dev
# install python dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache --upgrade -r requirements.txt
# chown all the files to the web user
RUN chown web:web -R $HOME