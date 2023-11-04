
# Dockerbird #

A Dockerized Django - Wagtail app

## Installation ###

### Install Docker Engine ###

    https://docs.docker.com/engine/install/

#### Linux Post-installation steps ####

    https://docs.docker.com/engine/install/linux-postinstall/

### Install Docker-compose ###

    https://docs.docker.com/compose/install/

## Setup ##

### Optional pre build configuration ###

#### Set language ####

.env

    LANGUAGE_CODE=sv
    TIME_ZONE=Europe/Stockholm
    POSTGRES_INITDB_ARGS='--locale=sv_SE'
    TZ='Europe/Stockholm'

### Build ###

    docker compose build --no-cache

    docker compose up

### Collectstatic ###

    docker compose exec web python manage.py collectstatic --no-input --clear

### Database migration ###

    docker compose exec web python manage.py migrate --no-input

### Search Index setup ###

    docker compose exec web python manage.py update_index

### Create a superuser ###

    docker compose exec web python manage.py createsuperuser

## Shut down ##

    # docker compose down
    # -v removes volumes

## Database managment ##

### Database export ###

    docker exec -i dockerbird_db_1 /bin/bash -c "pg_dump --username postgres --no-owner -x dbname" > bkp.psql

### Database import ###

    docker exec -i dockerbird_db_1 /bin/bash -c "PGPASSWORD=password psql --username postgres dbname" < bkp.psql

### Clear database ####

    docker compose exec web python manage.py flush --no-input

## Media managment ##

    docker exec dockerbird_web_1 ls

### Media export ###

    docker cp dockerbird_web_1:/home/web/media .

### Media import ###

    docker cp media dockerbird_web_1:/home/web/

## Use Compose in production ##

    https://docs.docker.com/compose/production/

## For development ##

    docker volume ls

    docker volume inspect dockerbird_postgres_data

    docker container ls

    docker exec -i dockerbird_db_1 bash

    docker compose exec web pip install -r requirements.txt

    docker exec dockerbird_web_1 ls

    docker images -f dangling=true

    docker image prune

## WIP ##

### Minikube ###

    echo -n "secret-string" | base64

    minikube delete

    minikube start

    eval $(minikube docker-env)

    minikube dashboard

    eval $(minikube docker-env)

    docker compose -f minikube.yml build --no-cache

    kubectl apply -f kubernetes/postgres/
    
    kubectl apply -f kubernetes/redis/

    kubectl apply -f kubernetes/django/

    kubectl get pods

    kubectl exec django-deployment-85984d6c5-89pnq -it -- bash

    chown web:web -R static

    chown web:web -R media

    kubectl exec django-deployment-85984d6c5-89pnq -it -- ./manage.py collectstatic

    kubectl exec django-deployment-85984d6c5-89pnq -it -- ./manage.py migrate

    kubectl exec django-deployment-85984d6c5-89pnq -it -- ./manage.py createsuperuser

    minikube service kubernetes-django-service

### WIP! ###

    minikube addons enable ingress

    kubectl apply -f kubernetes/ingress.yml

    minikube ip

    sudo nano /etc/hosts

    192.168.49.2  minikube.localhost
