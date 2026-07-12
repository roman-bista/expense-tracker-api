# Security Design

This document describes the security rules and authentication flow for the Expense Tracker API.

The goal is to protect user data, prevent unauthorized access, and follow backend security best practices.

---

# Authentication

The application uses **JWT (JSON Web Token)** authentication.

After a successful login:

- The server generates an access token.
- The client stores the token securely.
- The client sends the token in the Authorization header for protected requests.

Example:

```
Authorization: Bearer <access_token>
```

---

# Authorization

Every user can access **only their own data**.

Users are **not allowed** to:

- View another user's transactions.
- Edit another user's transactions.
- Delete another user's transactions.
- Access another user's categories.

The backend verifies ownership before performing any operation.

---

# Password Security

Passwords are never stored as plain text.

Business Rules:

- Passwords are hashed using **bcrypt** before storing them in the database.
- Password hashes cannot be reversed.
- Passwords are never returned in API responses.

---

# JWT Access Token

After login, the server returns a JWT access token.

Business Rules:

- Access token expires after **15 minutes**.
- Every protected endpoint requires a valid JWT.
- Expired tokens require the user to log in again (Refresh Token can be added in a future version).

---

# Input Validation

The backend validates all incoming requests.

Examples:

- Email must have a valid format.
- Password cannot be empty.
- Transaction amount must be greater than zero.
- Transaction type must be either **INCOME** or **EXPENSE**.
- Category name cannot be empty.
- Required fields cannot be missing.

Invalid requests return validation errors.

---

# Data Protection

Sensitive information should never be exposed.

The API must never return:

- Passwords
- Password hashes
- JWT secrets
- Database credentials

Only necessary user information is returned in responses.

---

# Environment Variables

Sensitive configuration is stored in environment variables.

Examples:

- DATABASE_URL
- SECRET_KEY
- ALGORITHM
- ACCESS_TOKEN_EXPIRE_MINUTES

These values are stored in a `.env` file and are **never committed** to GitHub.

---

# Access Control

The backend determines the authenticated user using the JWT token.

The client must never send:

```
user_id
```

The backend automatically assigns the authenticated user's ID when creating or updating data.

This prevents users from accessing or modifying another user's records.

---

# Common Security Threats

## SQL Injection

SQLAlchemy ORM will be used to reduce the risk of SQL injection by avoiding raw SQL queries.

---

## Broken Authentication

JWT authentication is required for all protected endpoints.

---

## Unauthorized Access

Every request verifies that the requested resource belongs to the authenticated user.

---

## Brute Force Attacks

Future Improvement:

- Limit repeated login attempts.
- Temporary account lock after multiple failed logins.

---

## Mass Assignment

The backend only accepts expected fields from client requests.

Unexpected fields are ignored or rejected.

---

## Sensitive Data Exposure

Passwords and secrets are never included in API responses.

---

# Future Improvements

Future versions may include:

- Refresh Tokens
- Email Verification
- Password Reset
- Two-Factor Authentication (2FA)
- Rate Limiting
- Audit Logs
- Session Management
- Login Notifications

---

# Security Decisions

## Why use JWT?

JWT allows the server to authenticate users without storing session data.

It is lightweight, scalable, and widely used for REST APIs.

---

## Why use bcrypt?

bcrypt securely hashes passwords and makes them difficult to crack using brute-force attacks.

---

## Why doesn't the client send user_id?

The authenticated user's identity is already available from the JWT token.

Accepting user_id from the client could allow users to manipulate another user's data.

Therefore, ownership is always determined by the backend.

---

## Why use environment variables?

Secrets such as database credentials and JWT keys should never be hardcoded in the source code.

Environment variables keep sensitive information separate from the application code.