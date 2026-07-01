# Expense Tracker API Design

## Features

## Database Tables

## Relationships

## API Endpoints

## Folder Structure

## Development Roadmap



Excellent. From this point onward, I'll act as your senior backend engineering mentor under those rules.

I'll optimize for one goal: **making you capable of designing production backend systems independently**, not just finishing an API.

### How we'll work

For every feature, we'll follow this engineering workflow:

1. **Requirements** – What problem are we solving?
2. **Business Logic** – What should happen?
3. **Database Design** – Tables, columns, constraints, relationships.
4. **API Design** – Endpoints, HTTP methods, request/response, status codes.
5. **Security** – Authentication, authorization, validation, attack vectors.
6. **Implementation** – Only after the design is sound.
7. **Review** – Think about edge cases, performance, and maintainability.

I will not give implementation code until we've completed the design.

---

# Your Project

**Expense Tracker API**

Production stack:

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Docker
* GitHub Actions
* Render

Treat this as if you're building software for real users.

---

# First Challenge

We are **not** creating code.

We are designing the system.

## Step 1 — Requirements

### Question 1

**What problem are we solving?**

Don't say:

> "An app to track expenses."

Think like you're writing a product requirements document.

Answer these questions:

1. Who are the users?
2. What pain are they experiencing?
3. What should they be able to do?
4. What should they NOT be able to do?
5. What is the MVP (Minimum Viable Product)?
6. What features are intentionally out of scope for version 1?

---

## Question 2

Imagine we have **10,000 users**.

Should every user be able to see everyone else's expenses?

Why?

---

## Question 3

Imagine this request:

```
POST /expenses
```

Should the client send:

```
user_id
```

inside the request body?

Why or why not?

---

## Question 4

What entities (real-world objects) exist in this system?

Don't think about tables yet.

Think about the business domain.

Example:

* User
* Expense
* Category

What else?

---

## Question 5

Suppose a user deletes a category named:

```
Food
```

There are already **1,000 expenses** using that category.

What should happen?

Think about multiple possible business rules and choose one.

---

### Constraints

Do **not** search online.

Do **not** jump to coding.

Reason through each answer. If your reasoning has gaps, I'll challenge it with questions rather than immediately correcting it.

Once we've validated the requirements together, we'll move to database design.
