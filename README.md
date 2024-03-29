# Carbon Projects API
A REST api serving carbon projects data

## Setup
**Running locally without Docker:**

Make sure [pyenv](https://github.com/pyenv/pyenv) is installed before running the below commands
```
pyenv virtualenv 3.8.12 <VENV_NAME>
pyenv activate <VENV_NAME>
pip install -r requirements-dev.txt
PYTHONPATH=src uvicorn src.main:app --reload
```
**Running locally with Docker:**

Make sure [Docker](https://docs.docker.com/engine/install/) is installed before running the below commands

```shell
docker build -t carbon-projercts-api .
docker run -p "8000:8000" carbon-projercts-api
```

## Endpoint

Once the server is running locally the following the `/projects` endpoint is accessible.
The OpenAPI docs can be viewed on `http://localhost:8000/docs`

1. Get all carbon projects data
```
curl http://localhost:8000/projects
```

2. Get carbon projects by ID

Please ensure the id provided is a uuid
```shell
curl http://localhost:8000/projects/{id}
```

## Design Considerations
- Selected REST for simplicity and resource orientated nature of the projects table
- Fast API, as I've built with it fairly recently, as well as nice in-built type validation and fast performance
- Avoided using an ORM i.e. sqlalchemy, as I find them restrictive. In this scenario probably overkill to not use one as the data model is simple.


## Scalability and Extensions
Increasing the size of the data and switching to a production system, I'd consider the following:
- Paginating or filtering the results via query params.
- Introducing caching - to prevent re-querying the table everytime the endpoint is called.
- Meta-data included in the response i.e. how many results are returned, next and previous page URLs.
- Adding CORs if there is frontend code accessing this API
- Adding security - i.e. Oauth
- 422 errors come from fastapi built-in, leaking too much information, would wrap this a simpler error to the user
