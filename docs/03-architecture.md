# Backend Architecture

## Overview

The Expense Tracker API follows a layered architecture. Each layer has a specific responsibility, making the application easier to understand, maintain, test, and extend.

The application consists of the following layers:

- API Layer
- Service Layer
- Database Layer
- Security Layer

This separation keeps business logic independent from database operations and HTTP requests.

---

# Project Structure

The project is organized into multiple folders instead of putting everything inside `main.py`.

This makes the project easier to maintain as it grows.

Example structure:

```
app/
├── api/
├── core/
├── database/
├── models/
├── schemas/
├── services/
├── crud/
├── dependencies/
├── main.py
```

### Responsibilities

**api/**
- Defines API endpoints (routers).

**core/**
- Application configuration.
- Security utilities.
- JWT settings.
- Environment settings.

**database/**
- Database connection.
- SQLAlchemy session.
- Base model.

**models/**
- SQLAlchemy ORM models.

**schemas/**
- Pydantic request and response models.

**services/**
- Business logic.

**crud/**
- Database queries.

**dependencies/**
- Shared FastAPI dependencies such as database sessions and authentication.

---

# Request Flow

Example request:

```
Client
    ↓
FastAPI
    ↓
Router
    ↓
Service Layer
    ↓
CRUD Layer
    ↓
SQLAlchemy
    ↓
PostgreSQL
```

Response:

```
PostgreSQL
    ↑
SQLAlchemy
    ↑
CRUD Layer
    ↑
Service Layer
    ↑
Router
    ↑
Client
```

Each layer performs only its own responsibility.

---

# Layers

### API Layer

Receives requests and validates input.

Responsibilities:

- Receive HTTP requests
- Validate request data
- Call service layer
- Return API responses

---

### Service Layer

Contains business logic.

Examples:

- Calculate balance
- Validate business rules
- Check ownership
- Process transactions

---

### CRUD Layer

Communicates with the database.

Responsibilities:

- Create records
- Read records
- Update records
- Delete records

No business logic should exist here.

---

### Database Layer

Responsible for:

- SQLAlchemy Engine
- Database Session
- Base Model
- PostgreSQL connection

---

# Configuration

Application settings should not be hardcoded.

Sensitive values are stored inside:

```
.env
```

Examples:

- DATABASE_URL
- SECRET_KEY
- ALGORITHM
- ACCESS_TOKEN_EXPIRE_MINUTES

This improves security and allows different configurations for development, testing, and production.

---

# Error Handling

The API should never expose internal server details.

Instead of returning database errors or stack traces, it should return appropriate HTTP status codes and user-friendly messages.

Example:

```
500 Internal Server Error
```

The detailed error should be written to server logs instead of being shown to the client.

---

# Logging

The application should record important events.

Examples:

- User login
- Failed login attempts
- Server errors
- Unexpected exceptions

Sensitive information such as passwords or JWT tokens must never be logged.

---

# Environments

The application should use separate environments.

### Development

Used while building the project.

### Testing

Uses a separate test database to avoid modifying real data.

### Production

Used by real users with production configuration and production database.

Keeping environments separate prevents accidental data loss and makes testing safer.

---

# Design Decisions

### Why separate folders?

Separating responsibilities keeps the code organized, reusable, and easier to maintain as the project grows.

---

### Why use layers?

Each layer has one responsibility.

This reduces coupling, improves readability, and makes testing easier.

---

### Why use environment variables?

Sensitive information should never be stored directly in the source code.

Using environment variables improves security and allows different settings for different environments.

---

### Why separate databases?

Development, testing, and production should never share the same database.

This prevents test data from affecting production data and allows safe experimentation.