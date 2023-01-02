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

You can view it on [link](https://task-manager.tk/)

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
1. Need to be [docker](https://www.docker.com/) is being installed
2. Download docker-compose.yml from this repository to work dir

      
      wget https://raw.githubusercontent.com/yuriy-kormin/python-project-52/main/docker-compose.yml

3. run command on work dir

      
      docker-compose up

5. enjoy app on http://localhost:8000

App uses postgresql in separate image, nginx and gunicorn as a web-server

### ADD

You can run this image in few more steps using service https://labs.play-with-docker.com/