# Carbon Projects API
The api returns carbon projects data

# Setup
pre-requisites:


**Running locally without Docker:**

Make sure [pyenv](https://github.com/pyenv/pyenv) is installed before running the below commands
```
pyenv virtualenv 3.8.12 <VENV_NAME>
pyenv activate <VENV_NAME>
pip install -r requirements-dev.txt
uvicorn src.main:app --reload
```
**Running locally with Docker:**

Make sure [Docker](https://docs.docker.com/engine/install/) is installed before running the below commands

```shell
docker build -t carbon-projects-api .
docker run -p "80:80" carbon_projects_api
```

# Endpoints

Once the server is running locally the following the projects
```
curl
```


# Considerations and Scalability
