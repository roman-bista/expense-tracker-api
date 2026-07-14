# Configuration Notes

## BaseSettings
Loads environment variables automatically.

## Settings
Represents the application's configuration.

## APP_NAME: str
Defines that APP_NAME must be a string loaded from .env.

##DATABASE URL
DATABASE_URL

Stores the connection string of the database.

It tells SQLAlchemy:
- Which database to connect to
- Which user to use
- Password
- Host
- Port
- Database name


 
SECRET_KEY

A secret string known only by the server.

It is used to create and verify JWT tokens.

Users should never know this key.


ALGORITHM
HS256 ALGORITHM WE WILL USE

ACCESS_TOKEN_EXPIRE_MINUTES: int
HOW MUCH TIME A TOKEN SHOULD BE ALIVE

DEBUG: bool
Controls whether the application
runs in development mode.

True
→ Shows detailed errors.

False
→ Hides internal errors from users.

model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()
OBJECT CREATED LATER WE CAN USE IT EVERYWHERE

## Why do we create `settings = Settings()`?

`Settings` is a class that knows how to read environment variables from the `.env` file.

By creating one global `settings` object, every module in the application can import the same configuration without reading the `.env` file repeatedly.

Example:

```python
from app.core.config import settings

print(settings.DATABASE_URL)