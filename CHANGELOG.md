# Changelog #

## tags ##

## commits ##

### 6 July 2025 ###

    doc: Readme improved and updated with Podman. Updated CHANGELOG.md.
    ci: Added a compose file for rootless Podman.
    chore: removed web/web/tasks.py
    ci: Use db postgres:alpine. python:3.12-slim.
    feat: Added Celery jobs publish_scheduled_pages and searchpromotions_garbage_collect.

### 5 May 2024 ###

    Minor Kubernetes volume changes. Env file and Django env settings improvements.

### 04 November 2023 ###

    Python 3.11 due to 3.12 bug. README cleanup. Removed extra django apps.

### 13 July 2022 ###

    Small improvments to docker-compose.yaml, Dockerfile, Django settings and dockerignore.

### 10 April 2022 ###

    License year update.

### 5 April 2022 ###

    Added Django-celcery-beat with redis. Removed home/app/web mapp in docker file script.

### 12 Mar 2022 ###

    Added a changlog. Changed from python-memcached and MemcachedCache to pymemcache and PyMemcacheCache. Improvements to Dockerfile.

### 28 Nov 2021 ###

    Refactory of app/Dockerfile, removed builder, using slim. Readme improvements, media managment, language settings.

### 16 Nov 2021 ###

    Updated Wagtail to 2.15. Added WAGTAILSEARCH_BACKENDS to settings.

### 15 Nov 2021 ###

    First commit.
