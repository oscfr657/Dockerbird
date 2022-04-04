
# Dockerbird #

A Dockerized Wagtail app

## Installation ###

### Install Docker Engine ###

    https://docs.docker.com/engine/install/

#### Post-installation steps for Linux ####

    https://docs.docker.com/engine/install/linux-postinstall/

### Install Docker-compose ###

    https://docs.docker.com/compose/install/

## Setup ##

### Optional pre build configuration ###

#### Set language ####

.env

    LANGUAGE_CODE=sv
    TIME_ZONE=Europe/Stockholm

.env.db

    POSTGRES_INITDB_ARGS='--locale=sv_SE'
    TZ='Europe/Stockholm'

### Build ###

    docker-compose build --no-cache

    docker-compose up

### Collectstatic ###

    docker-compose exec web python manage.py collectstatic --no-input --clear

### Database migration ###

    docker-compose exec web python manage.py migrate --no-input

### Search Index setup ###

    docker-compose exec web python manage.py update_index

### Create a superuser ###

    docker-compose exec web python manage.py createsuperuser

## Shut down ##

    # docker-compose down
    # -v removes volumes

## Database managment ##

### Database export ###

    docker exec -i dockerbird_db_1 /bin/bash -c "pg_dump --username db_user --no-owner -x db_name" > bkp.psql

### Database import ###

    docker exec -i dockerbird_db_1 /bin/bash -c "PGPASSWORD=db_password psql --username db_user db_name" < bkp.psql

### Clear database ####

    docker-compose exec web python manage.py flush --no-input

## Media managment ##

    docker exec dockerbird_web_1 ls

### Media export ###

    docker cp dockerbird_web_1:/home/app/media .

### Media import ###

    docker cp media dockerbird_web_1:/home/app/

## Use Compose in production ##

    https://docs.docker.com/compose/production/

## For development ##

    docker volume ls

    docker volume inspect dockerbird_postgres_data

    docker container ls

    docker exec -i dockerbird_db_1 bash

    docker exec dockerbird_web_1 ls

    docker images -f dangling=true

    docker image prune
