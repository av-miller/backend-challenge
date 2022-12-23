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

Database used in this example is SQLite. Please see Docker Compose section for Postgres. In order to get database 
created and loaded with seed data, please run the following command.

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


## Docker Compose

To run the service against a Postgres database in a Docker container, please start up docker compose with the following
command.

```bash
docker-compose up -d --build
```

Once the environment is up, please run database migrations using the below command.

```bash
docker-compose exec svc alembic upgrade head
```

Swagger API client should be available at the following URL.

http://localhost:8000/docs

Please stop docker compose environment when done with the below command.

```bash
docker-compose down -v
```