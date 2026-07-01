# Database Design

## Core Entities
- users
- expenses
- categories
- tags

## Relationships
- A user has many expenses.
- An expense belongs to one category and may have many tags.

## Notes
- Use UUIDs for primary keys where possible.
- Keep audit fields such as created_at and updated_at.
