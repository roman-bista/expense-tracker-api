Visualize it
Without config.py
.env
 │
 ├── auth.py ---------> os.getenv("SECRET_KEY")
 ├── database.py -----> os.getenv("DATABASE_URL")
 ├── security.py -----> os.getenv("ALGORITHM")
 ├── main.py ---------> os.getenv("DEBUG")
 └── email.py --------> os.getenv("SMTP_HOST")

Every file reads .env.

With config.py
                 .env
                   │
                   ▼
          app/core/config.py
                   │
          Settings Object
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
 database.py   security.py   auth.py
        from app.core.config import settings

Now every file uses the same settings object.

from app.core.config import settings

print(settings.DATABASE_URL)
print(settings.SECRET_KEY)
print(settings.DEBUG)
<--------------------------------------------------------->
<--------------------------------------------------------->