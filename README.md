# FastAPI CRUD API with JWT, PostgreSQL, and Docker

A production-style backend API built using FastAPI with authentication and containerization.

## Features

- User authentication using JWT
- CRUD operations for tasks
- PostgreSQL database
- SQLAlchemy ORM
- Dockerized setup
- Environment variable configuration

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- JWT Authentication

## Setup

Clone repository:

git clone https://github.com/username/fastapi-docker-postgres-crud.git

Run with Docker:

docker-compose up --build

API will start at:

http://localhost:8000/docs

## API Endpoints

POST /users/register  
POST /users/login  
POST /tasks  
GET /tasks  
DELETE /tasks/{id}

## Architecture

Client → FastAPI → SQLAlchemy → PostgreSQL
