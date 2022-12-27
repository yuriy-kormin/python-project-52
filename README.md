<style>
red { color: red }
</style>
### Badges:
[![Actions Status](https://github.com/yuriy-kormin/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/yuriy-kormin/python-project-52/actions)
[![Actions Status](https://github.com/yuriy-kormin/python-project-52/workflows/linter-run/badge.svg)](https://github.com/yuriy-kormin/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0e46f885a1a6e58247b8/maintainability)](https://codeclimate.com/github/yuriy-kormin/python-project-52/maintainability)
[![test](https://github.com/yuriy-kormin/python-project-52/actions/workflows/django-test.yml/badge.svg)](https://github.com/yuriy-kormin/python-project-52/actions/workflows/django-test.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0e46f885a1a6e58247b8/test_coverage)](https://codeclimate.com/github/yuriy-kormin/python-project-52/test_coverage)

# Task Manager

It's a classic task manager project with opportunity to set marks and set performer for each task.

## STATUS

Project <red>in development</red> right now, but You can view work copy on [link](https://task-manager.tk/)

## INSTALLATION
### Local option
Need to  [poetry](https://python-poetry.org/docs/#installation) is to be installed 


 
    git clone https://github.com/yuriy-kormin/python-project-52.git
    cd python-project-52
    make install
    make migrate
    make start

enjoy app on http://localhost:8000

### Settings
Environment variables
- database
- django-secret 
- rollbar token

can be set in environment or by rename file .env_example and set values in it. 
    
    /.env_example -> /.env

### Docker
Need to be [docker](https://www.docker.com/) is being installed 

After complete install, just several commands


    docker pull tork83/task-manager
    docker run -p 8000:8000 tork83/task-manager

enjoy app on http://localhost:8000

Currently the application uses sqlite as the database - I plan to rebuild this image to use Postgres as the default database in a separate image.

