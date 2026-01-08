# Changelog #

## tags ##

## commits ##

### 8 January 2026 ###

    doc: Updated CHANGELOG.md.
    doc: Changed Kompose outpath part of README.md.
    ci: Removed kubernetes wip alternative to use Kompose instead.
    ci: Improved docker-compose.yml with Kompose labels, ports, deploy resources and web image name.

### 5 January 2026 ###

    doc: Updated CHANGELOG.md.
    doc: Updated README.md with Minikube rootless and Kompose etc.
    feat: Added Minikube rootless.
    feat: Improved podman-compose.yml with kompose labels, ports, volumes and web image name.
    chore: improved .gitignore and .dockerignore.
    ci: docker-compose versionless nginx:alpine.
    feat: Nginx log off for robots.txt
    feat: Added CSRF_TRUSTED_ORIGINS

### 2 September 2025 ###

    feature: Improved settings.py and .env
    ci: Versionless nginx:alpine
    refactor: Tiny improvement to and moved Dockerfile to root level.

### 9 July 2025 ###

    doc: Updated CHANGELOG.md.
    ci: Improved compose files to only create and use one custom image.

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
