<!-- ![image](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg "CalVer")
![image](https://travis-ci.org/devsetgo/starlette-SRTDashboard.svg "Build Status")
![image](coverage.svg "Code Coverage") -->
Python:
![image](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg "CalVer")
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

CI/CD Pipeline:
[![codecov](https://codecov.io/gh/devsetgo/starlette-SRTDashboard/branch/master/graph/badge.svg)](https://codecov.io/gh/devsetgo/starlette-SRTDashboard)
[![Actions Status](https://github.com/devsetgo/starlette-SRTDashboard/workflows/Run%20Tests/badge.svg)](https://github.com/devsetgo/starlette-SRTDashboard/actions)
[![Actions Status](https://github.com/devsetgo/starlette-SRTDashboard/workflows/Docker%20Latest/badge.svg)](https://github.com/devsetgo/starlette-SRTDashboard/actions)


SonarCloud:
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=devsetgo_starlette-SRTDashboard&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=devsetgo_starlette-SRTDashboard)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=devsetgo_starlette-SRTDashboard&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=devsetgo_starlette-SRTDashboard)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=devsetgo_starlette-SRTDashboard&metric=alert_status)](https://sonarcloud.io/dashboard?id=devsetgo_starlette-SRTDashboard)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=devsetgo_starlette-SRTDashboard&metric=bugs)](https://sonarcloud.io/dashboard?id=devsetgo_starlette-SRTDashboard)

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
# Starlette - SRTDashboard Template
Note: The template has ~2900 issues according to SonarCloud
Utilizing Starlette to render the [SRTDashboard](https://github.com/devsetgo/srtdash-admin-dashboard) admin template. This is a basic example to be used as the base/skeleton/template for Starlette applciations.

![Starlette SRTDashboard](screenshots/image_1.PNG)

### Use it
- git clone https://github.com/devsetgo/starlette-SRTDashboard
- create a virtualenv on linux or Windows Subsystem Linux

#### Run APP
First Change directory to app

UVICORN
    Development:
~~~~
    uvicorn main:app --port 5000 --reload
    python3 main.py
~~~~
    Production:
~~~~
    uvicorn main:app --workers 2
    gunicorn -c gunicorn_cfg.py main:app
    # Note: gunicorn is the config for the dockerfile
~~~~

Docker
~~~~
    Docker: docker pull mikeryan56/starlette-srtdashboard:latest (not implemented)
~~~~

#### Run Tests
~~~~
python3 -m pytest
~~~~

#### Create coverage badge
~~~~
    coverage-badge -o coverage.svg -f
~~~~

#### Pre-Commit & Hooks
~~~~
    - Follow install instructionsL: [https://pre-commit.com/#install](https://pre-commit.com/#install)
    - pre-commit install
    - pre-commit run -a
~~~~

## Issues/Bugs

- [ ] cleanup

## TODO

- [x] Refactor by endpoint (sample, user, etc..)
- [x] Create tests
    - [x] Minimum of 80%
    - [ ] Exception Testing
    - [ ] Mock [requests](https://2.python-requests.org/en/master/) call
- [x] Better organization
    - [ ] Use of Endpoints (equivalent to Flask Blueprints)
- [ ] Configuration Scripts

- [ ] Access Controls
  - [ ] Add Access controls
  - [ ] Signup functionality

- [x] Gunicorn/Uvicorn configuration
- [x] Logging (using [Loguru](https://github.com/Delgan/loguru))
- [X] Setup CI/CD Pipeline for test and deployment
    - ~~[X] [Travis-CI](https://travis-ci.org)~~ ***replaced by Github Actions***
    - [X] [SonarCloud](https://sonarcloud.io)
    - [x] [Github Actions](https://github.com/features/actions) found in .github/workflow/actions
        - [x] tests - matrix run of Python 3.6 and 3.7
            - [x] CodeCove.io upload
        - [x] docker-rc - docker build and push when pull request approved for release-candidate branch (calendar version - rc)
        - [x] docker-master - docker build and push when pull request approved for master branch (calender version and latest)
        - [x] ensure docker build only happens after pull_request approved and merged into higher branch
- [ ] [Twelve Factor App](https://12factor.net/) ready
- [ ] Build a [cookiecutter](https://github.com/audreyr/cookiecutter) template for
- [ ] Add code comments
- [ ] Websocket example

- Docker
  - [ ] Docker Image
  - [x] Docker-Compose
    - [ ] Docker Swarm settings
  - [ ] Kubernetes Kompose

- Tutorials/Documentation
  - [ ] Basic Overview
  - [ ] Explantion of Functions
  - [ ] Explantion of Configuration

### Screenshots
![Starlette SRTDashboard](screenshots/image_1.PNG)
![Starlette SRTDashboard](screenshots/image_2.PNG)
![Starlette SRTDashboard](screenshots/image_3.PNG)
![Starlette SRTDashboard](screenshots/image_4.PNG)
![Starlette SRTDashboard](screenshots/image_5.PNG)
