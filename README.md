## Tech Stack

**Language:** Python 3

**Framework:** FastAPI

**Database:** MySQL | PostgreSQL | SQlite

## Features

 - Authors
 - Books
 - Associations

## Installation
copy file .env.exmaple and rename it to .env and config your database    
```bash
  DB_CONNECTION=
  DB_HOST=
  DB_PORT=
  DB_DATABASE=
  DB_USERNAME=
  DB_PASSWORD=
```
install dependencies
```bash
  pip install -r requirements.txt
```
create migration. once you run it, it will create all tables, so you don't have to run one by one
```bash
  alembic revision --autogenerate -m "create table"
```
run migration
```bash
  alembic upgrade head
```

## Run Locally

Start the server

```bash
  uvicorn main:app --reload
```
or
```bash
  python main.py
```
when you start the server, it will run the seeder automatically

## Running Tests

To run tests, run the following command

```bash
  pytest
```

## API Reference

### Authors
Retrieve a list of all authors.
```http
  GET /authors
```
Retrieve details of a specific author.
```http
  GET /authors/{id}
```

| Parameter | Type     | Description. |
| :-------- | :------- | :------------|
| `id`      | `int`    | **Required**.|

Create a new author.
```http
  POST /authors
```

| Request Body| Type     | Description  |
| :--------   | :------- | :------------|
| `name`      | `string` | **Required**.|
| `bio`       | `string` | **Required**.|
| `birth_date`| `date`   | **Required**.|

Update an existing author.
```http
  PUT /authors/{id}
```
| Parameter | Type     | Description. |
| :-------- | :------- | :------------|
| `id`      | `int`    | **Required**.|

| Request Body| Type     | Description  |
| :--------   | :------- | :------------|
| `name`      | `string` | **Required**.|
| `bio`       | `string` | **Required**.|
| `birth_date`| `date`   | **Required**.|

Delete an author.
```http
  DELETE/authors/{id}
```
| Parameter | Type     | Description. |
| :-------- | :------- | :------------|
| `id`      | `int`    | **Required**.|

### Books
Retrieve a list of all books.
```http
  GET /books
```
Retrieve details of a specific book.
```http
  GET /books/{id}
```
| Parameter | Type     | Description. |
| :-------- | :------- | :------------|
| `id`      | `int`    | **Required**.|

Create a new book.
```http
  POST /books
```
| Request Body. | Type     | Description  |
| :--------     | :------- | :------------|
| `title`       | `string` | **Required**.|
| `description` | `string` | **Required**.|
| `publish_date`| `date`   | **Required**.|
| `author_id`.  | `int`    | **Required**.|

Update an existing book.
```http
  PUT /books/{id}
```
| Parameter | Type     | Description. |
| :-------- | :------- | :------------|
| `id`      | `int`    | **Required**.|

| Request Body. | Type     | Description  |
| :--------     | :------- | :------------|
| `title`       | `string` | **Required**.|
| `description` | `string` | **Required**.|
| `publish_date`| `date`   | **Required**.|
| `author_id`.  | `int`    | **Required**.|

Delete a book.
```http
  DELETE/books/{id}
```
| Parameter | Type     | Description. |
| :-------- | :------- | :------------|
| `id`      | `int`    | **Required**.|

### Associations
Retrieve all books by a specific
```http
  GET /authors/{id}/books
```
| Parameter | Type     | Description. |
| :-------- | :------- | :------------|
| `id`      | `int`    | **Required**.|
