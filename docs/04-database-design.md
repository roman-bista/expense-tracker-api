# Database Design

## 1. Core Entities

The application will have the following core entities:

- User
- Transaction
- Category

> **Design Decision:** Instead of creating separate `Income` and `Expense` tables, the application will use a single **Transaction** entity. Each transaction will have a `type` field (`INCOME` or `EXPENSE`). This keeps the design simple and makes reports and dashboards easier to generate.

---

## 2. Relationships

### User ↔ Transaction

- One user can have many transactions.
- Each transaction belongs to only one user.

Relationship:

```
User (1) -------- (Many) Transactions
```

---

### Category ↔ Transaction

- One category can have many transactions.
- Each transaction belongs to one category.

Relationship:

```
Category (1) -------- (Many) Transactions
```

---

## 3. User Entity

Each user will have the following information:

- id
- first_name
- last_name
- email
- password (hashed)
- created_at
- updated_at
- is_active

---

## 4. Transaction Entity

Each transaction will contain:

- id
- title
- amount
- type (Income / Expense)
- description (optional)
- transaction_date
- category_id
- user_id
- created_at
- updated_at

---

## 5. Category Entity

Each category will contain:

- id
- name
- color (optional)
- description (optional)
- user_id
- created_at
- updated_at

> **Design Decision:** Categories are personal. Each user can create and manage their own categories. For example:

Roman:
- Food
- Gym
- Netflix

Alice:
- Food
- Travel
- Rent

Both users are allowed to have a category named **Food** because categories belong to individual users.

---

# Constraints

## User

- Email must be unique.
- Email cannot be empty.
- Password cannot be empty.
- First name cannot be empty.
- Last name cannot be empty.

---

## Transaction

- Amount is required.
- Amount must be greater than zero.
- Transaction type is required.
- Transaction date is required.
- Category is required.
- Every transaction must belong to a user.

---

## Category

- Category name cannot be empty.
- Category names must be unique **for each user**.
- Different users may use the same category name.

Example:

Roman
```
Food
```

Alice
```
Food
```

This is allowed.

Roman
```
Food
Food
```

This is **not** allowed.

---

# Foreign Keys

Transaction table:

- user_id → Users.id
- category_id → Categories.id

Category table:

- user_id → Users.id

Relationships are created using IDs instead of names because IDs never change, while names can be edited.

---

# Design Decisions

### Why use one Transaction table?

Using a single Transaction table makes the application easier to maintain and extend.

Benefits:

- One transaction history for the user.
- Easier monthly and yearly reports.
- Easier balance calculations.
- Simpler dashboard queries.
- New transaction types (Loan, Transfer, Investment, etc.) can be added without creating new tables.

---

### Why use personal categories?

Every user has different spending habits.

Example:

Roman
- Gym
- Coffee
- Netflix

Alice
- Rent
- Kids
- Pets

Allowing personal categories gives users more flexibility and avoids unnecessary restrictions.

---

### Why use IDs instead of names?

Names can change.

For example:

```
Roman
```

can become

```
Roman Bista
```

The user's **id** never changes, so relationships remain consistent and reliable.
