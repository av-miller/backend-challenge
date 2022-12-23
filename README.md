# Backend Challenge

## Dependencies

Poetry is used for dependency management. Please install Poetry package management by running the below command as 
described in [Poetry documentation](https://python-poetry.org/docs/).

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

To install dependencies, please run the following command.

```bash
poetry install
```

## Database

Database used in this example is SQLite. In order to get database created and loaded with seed data, please run the 
following command.

```bash
alembic upgrade head
```

This should create a file called `backend.db` containing required tables.

## Service

Service is implemented using FastAPI. Please run the following command to start up the service.

```bash
uvicorn app.main:app --reload
```

Once the service starts, you should be able to access Swagger API client at the below URL.

http://localhost:8000/docs
