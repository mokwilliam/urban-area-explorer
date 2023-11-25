# Urban Area Explorer

This small Data Engineering project focuses on aggregating, analyzing, and visualizing data related to urban areas sourced from [Teleport](http://developers.teleport.org) website. The goal is to build a comprehensive urban area explorer that showcases various aspects such as housing, safety, education, economy, and more. Leveraging continuous integration and continuous deployment (CI/CD) practices, the project provide a dashboard for exploring urban area data and understanding regional differences.

Help from:

- [Poetry](https://python-poetry.org)
- [Flask](https://github.com/pallets/flask/)
- [CircleCI](https://circleci.com/docs/)

## Overview

In this project, we are creating a web app that offers users a dashboard for exploring urban area data and understanding regional differences.

## Steps followed

### 0. Installation & Setup

- Poetry project

```bash
pip install poetry

# `poetry init --no-interaction` to initialize a pre-existing project
poetry new backend --name="app"
cd backend
poetry add flask
# pip install python-dotenv to use .env file
# `poetry shell` to access the environment in the terminal and `exit` to exit the environment
```

### Extra: Setup of CircleCI

CircleCI is a continuous integration and continuous delivery (CI/CD) platform that automates the building, testing, and deployment of projects. It is a great tool to automate the testing and deployment of the project.

To setup CircleCI, we need to create a `.circleci` folder at the root of the project and add a `config.yml` file inside. The `config.yml` file contains the configuration for the CI/CD pipeline.

### Extra: Setup of pytest

Once the test files are written, we can run the tests.

```bash
pip install pytest

# To run tests
pytest
```

### Extra: Setup of pre-commit

```bash
pip install pre-commit
```

Once the `.pre-commit-config.yaml` completed, we need to set up the git hooks scripts.

```bash
pre-commit install
```
