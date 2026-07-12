# API Design

This document defines the REST API endpoints for the Expense Tracker API. The API follows REST principles and returns appropriate HTTP status codes for each request.

---

# Authentication

## Register User

**Endpoint**

```
POST /auth/register
```

**Description**

Creates a new user account.

---

## Login

**Endpoint**

```
POST /auth/login
```

**Description**

Authenticates the user and returns a JWT access token.

---

## Logout

**Endpoint**

```
POST /auth/logout
```

**Description**

Logs the user out of the application.

---

## Get Current User

**Endpoint**

```
GET /users/me
```

**Description**

Returns information about the currently authenticated user.

---

## Refresh Token (Future Feature)

**Endpoint**

```
POST /auth/refresh
```

**Description**

Generates a new access token using a refresh token.

---

# Transactions

## Create Transaction

**Endpoint**

```
POST /transactions
```

**Description**

Creates a new income or expense transaction.

---

## Get All Transactions

**Endpoint**

```
GET /transactions
```

**Description**

Returns all transactions belonging to the authenticated user.

---

## Get Transaction by ID

**Endpoint**

```
GET /transactions/{transaction_id}
```

**Description**

Returns details of a specific transaction.

---

## Update Transaction

**Endpoint**

```
PATCH /transactions/{transaction_id}
```

**Description**

Updates selected fields of a transaction.

> PATCH is used because users usually update only a few fields instead of replacing the entire transaction.

---

## Delete Transaction

**Endpoint**

```
DELETE /transactions/{transaction_id}
```

**Description**

Permanently deletes a transaction.

---

# Categories

## Create Category

```
POST /categories
```

Creates a new personal category.

---

## Get Categories

```
GET /categories
```

Returns all categories created by the authenticated user.

---

## Update Category

```
PATCH /categories/{category_id}
```

Renames or updates a category.

---

## Delete Category

```
DELETE /categories/{category_id}
```

Deletes a category if it is not currently used by any transaction.

---

# Dashboard

## Dashboard Summary

```
GET /dashboard
```

Returns dashboard information including:

- Total Income
- Total Expenses
- Remaining Balance
- Monthly Summary
- Recent Transactions

The backend performs all calculations and returns only the required data.

---

# Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 OK | Request completed successfully |
| 201 Created | Resource created successfully |
| 204 No Content | Resource deleted successfully |
| 400 Bad Request | Invalid request |
| 401 Unauthorized | User is not authenticated or credentials are incorrect |
| 403 Forbidden | User does not have permission to access the resource |
| 404 Not Found | Requested resource does not exist |
| 422 Unprocessable Entity | Validation error |

---

# Request & Response Design

## Create Transaction Request

The client should send:

- title
- amount
- type (Income or Expense)
- category_id
- description (optional)
- transaction_date

### Important Design Decision

The client **must not** send `user_id`.

The backend identifies the authenticated user from the JWT access token and automatically assigns the correct `user_id`.

This prevents users from creating or modifying transactions belonging to other users.

---

## Response

After a successful request, the API returns:

- Success message
- Newly created transaction
- Generated transaction ID

---

# Filtering

The Transactions API should support filtering by:

- Month
- Year
- Category
- Transaction Type (Income / Expense)

Future improvements may include:

- Pagination
- Sorting
- Search by title or description

---

# API Design Decisions

### Why does the client not send `user_id`?

The backend already knows the authenticated user through the JWT token.

Allowing the client to send `user_id` could let malicious users create or modify another user's data.

Therefore, ownership is always determined by the backend.

---

### Why use PATCH instead of PUT?

PATCH updates only the fields that need to change.

PUT replaces the entire resource.

Since users usually edit only one or two fields of a transaction, PATCH is more efficient and follows REST best practices.

---

### Why create a separate Dashboard endpoint?

The dashboard requires calculated values such as total income, total expenses, and remaining balance.

Instead of sending thousands of transactions to the frontend, the backend performs the calculations and returns only the required summary data.

This improves performance and reduces network traffic.