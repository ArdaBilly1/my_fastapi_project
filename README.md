# FastAPI Transaction Management System

A FastAPI-based transaction management system built with async SQLAlchemy and clean architecture principles. This project is currently being developed to test idempotency patterns in API design.

> **Note:** This library is still a work in progress and is being used for testing idempotency implementations.

## Features

- ✅ Async/await support with FastAPI
- ✅ SQLite database with async SQLAlchemy (aiosqlite)
- ✅ Clean architecture (Repository, Service, Model, Schema layers)
- ✅ RESTful API endpoints for transaction management
- ✅ Automatic database table creation on startup
- 🚧 Idempotency implementation (in progress)

## Project Structure

```
.
├── db/
│   └── database.py          # Database connection and session management
├── models/
│   └── transactions.py      # SQLAlchemy ORM models
├── repositories/
│   └── transaction_repo.py  # Data access layer
├── schemas/
│   ├── transactions.py      # Pydantic request/response schemas
│   └── response.py          # Standard API response wrapper
├── services/
│   └── transaction_svc.py   # Business logic layer
├── main.py                  # FastAPI application entry point
├── makefile                 # Development commands
└── system-fastapi.db        # SQLite database file
```

## Architecture

The project follows a layered architecture:

1. **Models** (`models/`) - SQLAlchemy ORM entities
2. **Schemas** (`schemas/`) - Pydantic models for request/response validation
3. **Repositories** (`repositories/`) - Data access layer with database operations
4. **Services** (`services/`) - Business logic layer
5. **API Routes** (`main.py`) - FastAPI endpoints

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy (with async support)
- aiosqlite
- Pydantic
- Uvicorn

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd my_fastapi_project
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi sqlalchemy aiosqlite pydantic uvicorn
```

## Running the Application

### Using Makefile (recommended)

```bash
make run-local
```

### Using Uvicorn directly

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check

```http
GET /
```

**Response:**
```json
{
  "status": "success",
  "message": "OK",
  "data": null
}
```

### Create Transaction

```http
POST /transactions
```

**Request Body:**
```json
{
  "amount": 1000,
  "description": "Payment for service"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "OK",
  "data": {
    "id": 1,
    "amount": 1000,
    "description": "Payment for service"
  }
}
```

### Get All Transactions

```http
GET /transactions
```

**Response:**
```json
{
  "status": "success",
  "message": "OK",
  "data": [
    {
      "id": 1,
      "amount": 1000,
      "description": "Payment for service"
    }
  ]
}
```

### Get Transaction by ID

```http
GET /transactions/{trx_id}
```

**Response:**
```json
{
  "id": 1,
  "amount": 1000,
  "description": "Payment for service"
}
```

### Delete Transaction

```http
DELETE /transactions/{trx_id}
```

**Response:**
```json
{
  "id": 1,
  "amount": 1000,
  "description": "Payment for service"
}
```

## Database

The application uses SQLite with async support via `aiosqlite`. The database file is automatically created as `system-fastapi.db` in the project root.

Tables are automatically created on application startup using SQLAlchemy's `create_all()` method.

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing (Idempotency Focus)

This project is being used to test and implement idempotency patterns. Future updates will include:

- [ ] Idempotency keys for transaction creation
- [ ] Request deduplication mechanism
- [ ] Idempotency testing suite
- [ ] Race condition handling

## Development

The project uses a clean architecture approach with clear separation of concerns:

- **Repository Layer**: Handles all database operations
- **Service Layer**: Contains business logic and orchestration
- **Schema Layer**: Defines data validation and serialization
- **API Layer**: Exposes HTTP endpoints

## Future Enhancements

- [ ] Complete idempotency implementation
- [ ] Add authentication and authorization
- [ ] Implement request validation middleware
- [ ] Add comprehensive error handling
- [ ] Create unit and integration tests
- [ ] Add logging and monitoring
- [ ] Database migrations with Alembic
- [ ] Docker containerization

## Contributing

This is a learning project focused on testing idempotency patterns. Contributions and suggestions are welcome!

