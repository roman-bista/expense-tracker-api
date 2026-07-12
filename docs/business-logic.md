1. User Registration

Users must create an account before using the application.

During registration, users will provide:

First name
Last name
Email address
Password

Business Rules:

Each email address must be unique.
Two users cannot register with the same email.
Passwords must never be stored as plain text. They should be securely hashed before saving to the database.
After successful registration, the user will be redirected to the login page to sign in.
2. User Login

Registered users can log in using their email and password.

Business Rules:

Users must provide the correct email and password.
If the password is incorrect, login will fail.
Users can use the "Forgot Password" feature if they forget their password (future feature).
After successful login, the server will issue a JWT access token.
The access token will expire after a limited time (for example, 10–15 minutes) for better security.

3. Income Management

Users can record every source of income.

Business Rules:

Users can add multiple income records.
Income amount must be greater than zero.
Negative income is not allowed.
Users can categorize income if needed.
Users can edit or delete income records if they entered incorrect information.
4. Expense Management

Users can record every expense they make.

Business Rules:

Users must enter:
Amount
Category
Date
Description (optional)
Expense amount must be greater than zero.
Zero or negative expense amounts are not allowed.
Future dates are not allowed.
Every expense must belong to a category.
If the selected category does not exist, the expense cannot be created.
5. Editing Transactions

Users can update their income and expense records.

Business Rules:

Users can edit the amount, category, description, and date if they entered incorrect information.
Changes will overwrite the previous values.
Version history will not be maintained in Version 1.
6. Deleting Transactions

Users can permanently delete their own income or expense records.

Business Rules:

Only the owner of the transaction can delete it.
Deleted transactions cannot be recovered.
Soft delete or recycle bin functionality may be added in future versions.
7. Category Management

Users can organize their expenses using categories.

Business Rules:

Users can create new categories.
Users can rename existing categories.
Users cannot delete a category if it is currently being used by one or more expenses.
Users must first move or delete those expenses before deleting the category.
8. Dashboard

The dashboard gives users a quick overview of their financial status.

The dashboard will display:

Total income
Total expenses
Remaining balance
Monthly spending summary
Recent transactions
9. Security Rules

The application must protect every user's financial data.

Business Rules:

Users can access only their own data.
One user cannot view or modify another user's transactions.
The client must never send user_id when creating or updating transactions.
The backend will identify the authenticated user from the JWT token.
Every protected endpoint requires authentication.
10. Validation Rules

The application will validate all user input before saving it.

Validation Rules:

Expense amount must be greater than zero.
Income amount must be greater than zero.
Email addresses must be unique.
Category name cannot be empty.
Transaction date must be a valid date.
Required fields cannot be empty.
Invalid requests will return appropriate validation errors.
Senior Engineer Note

This is a Version 1 business logic document. As we build the project, we may update these rules if we discover better approaches or new requirements. The goal is to have a clear understanding of how the application should behave before designing the database or writing any code.