1. Engine
Think of it as the manager.
Responsibilities:
Knows how to connect to PostgreSQL
Owns the connection pool
Doesn't execute queries itself
Lives for the entire application
One Engine.

2. Connection Pool
This is where performance comes from.
Suppose 100 users use your API.
Without a pool:
User1
Open TCP Connection

User2
Open TCP Connection

User3
Open TCP Connection

...

100 TCP Connections
Very slow.

1. Engine
Think of it as the manager.
Responsibilities:
Knows how to connect to PostgreSQL
Owns the connection pool
Doesn't execute queries itself
Lives for the entire application
One Engine.
2. Connection Pool
This is where performance comes from.
Suppose 100 users use your API.
Without a pool:
User1
Open TCP Connection

User2
Open TCP Connection

User3
Open TCP Connection

...

100 TCP Connections
Very slow.

3. Connection
A Connection is one actual communication channel with PostgreSQL.
Think:
Python
────────────
PostgreSQL

4. Session
This is what you work with.
A Session:
keeps track of ORM objects
executes queries
commits
rolls back
closes itself
You almost never touch ra




## Engine

The Engine is the main object that manages communication with the database.

Responsibilities:
- Knows how to connect to PostgreSQL.
- Manages the Connection Pool.
- Creates database connections when needed.
- Lives for the entire lifetime of the application.


Why only one Engine?

Creating an Engine is expensive because it creates and manages the Connection Pool.

Instead of creating a new Engine for every request, the application creates one Engine when it starts and all requests reuse it.


## Connection Pool

The Connection Pool stores reusable database connections.

Instead of creating a new database connection for every request, SQLAlchemy reuses existing connections.

Benefits:
- Better performance
- Faster requests
- Lower resource usage

Without a Connection Pool:

Every request creates a new database connection.

This is slow and expensive.

With a Connection Pool:

Connections are reused, making the application much faster.

## Session

A Session represents one conversation with the database.

Every request gets its own Session.

Responsibilities:
- Execute queries
- Track ORM objects
- Commit changes
- Rollback on errors
- Close when the request finishes

Each request should have its own Session to keep database operations isolated.

This prevents one user's work from affecting another user's request.

## Session Factory

The Session Factory is created using sessionmaker().

Its job is to create new Session objects whenever the application needs one.

Instead of manually creating Sessions, we ask the Session Factory to create them.
## Flow

.env
↓

config.py
↓

settings object
↓

create_engine()

↓

Engine

↓

Connection Pool

↓

Session Factory

↓

Session

↓

PostgreSQL




<-------------------------------------------------->
<-------------------------------------------------->
SessionLocal = sessionmaker(bind=engine)
visual:

Engine
   ▲
   │
bind
   │
Session Factory
   │
   ▼
Session A

Session B

Session C
<--------------------------------->
<--------------------------------->
get_db() centralizes database session management. Instead of every endpoint creating and closing its own Session, all endpoints reuse the same logic. This reduces duplicate code, ensures every Session is closed correctly, and keeps endpoint code focused on business logic rather than database lifecycle management.
Who creates the Session?
get_db()
Who should close it?
get_db()
Rule:
The component that creates a resource should usually be responsible for cleaning it up.
Client
   │
   ▼
FastAPI
   │
   ▼
get_db()
   │
   ▼
Session
   │
   ▼
Engine
   │
   ▼
Connection Pool
   │
   ▼
PostgreSQL
<--------------------------------->
<--------------------------------->
Imagine your frontend sends:
POST /login
The flow is:
User clicks Login
        │
        ▼
Browser sends HTTP Request
        │
        ▼
FastAPI receives request
        │
        ▼
Find matching endpoint
        │
        ▼
Run login() function
        │
        ▼
Validate user
        │
        ▼
Query PostgreSQL
        │
        ▼
Return JWT
        │
        ▼
Browser receives response

Each endpoint should have one responsibility.



User clicks "Transactions"

        ↓

Browser sends

GET /transactions

        ↓

FastAPI receives request

        ↓

Routing

Find matching endpoint

        ↓

Authenticate user
(Check JWT)

        ↓

Endpoint executes

        ↓

SQLAlchemy creates SQL

        ↓

PostgreSQL executes SQL

        ↓

PostgreSQL returns data

        ↓

SQLAlchemy converts rows into Python objects

        ↓

FastAPI converts Python objects into JSON

        ↓

Browser receives JSON

        ↓

Frontend displays transactions

401 Unauthorized means the user could not be authenticated, such as when the JWT is missing, invalid, or expired.
403 Forbidden means the user has already been authenticated, but does not have permission to perform the requested action.
Request Arrives
        │
        ▼
JWT Present?
        │
   No ───────► 401 Unauthorized
        │
       Yes
        │
        ▼
JWT Valid?
        │
   No ───────► 401 Unauthorized
        │
       Yes
        │
        ▼
Resource Exists?
        │
   No ───────► 404 Not Found
        │
       Yes
        │
        ▼
Does User Own Resource?
        │
   No ───────► 403 Forbidden
        │
       Yes
        │
        ▼
Perform Action
        │
        ▼
200 OK / 201 Created / 204 No Content


| Status Code                   | Meaning                                 | Example                           |
| ----------------------------- | --------------------------------------- | --------------------------------- |
| **200 OK**                    | Request succeeded                       | Get transactions                  |
| **201 Created**               | New resource created                    | Register user, create transaction |
| **204 No Content**            | Success, but no response body           | Delete transaction                |
| **400 Bad Request**           | Invalid request from client             | Invalid input                     |
| **401 Unauthorized**          | User is not authenticated               | Missing or expired JWT            |
| **403 Forbidden**             | User authenticated but lacks permission | Access another user's data        |
| **404 Not Found**             | Requested resource doesn't exist        | Transaction ID doesn't exist      |
| **500 Internal Server Error** | Unexpected server error                 | Database crashed                  |



autocommit=False

SQLAlchemy does not automatically save changes.

The developer decides when to save data by calling:

db.commit()

This helps keep the database consistent and supports transactions.


Setting	Meaning
autocommit=False------>	Don't automatically save changes. Wait for db.commit().
autoflush=False------->	 Don't automatically flush pending SQL before queries. Let the developer control it.

Client Request
      │
      ▼
FastAPI
      │
      ▼
Depends(get_db)
      │
      ▼
get_db()

db = SessionLocal()

      │
      ▼
yield db
      │
      ▼
Endpoint receives:

db: Session
      │
      ▼
Endpoint queries database
      │
      ▼
Endpoint returns response
      │
      ▼
get_db() resumes
      │
      ▼
db.close()

-----------------------------------------------------
-----------------------------------------------------

Python Class

↓

Inherits Base

↓

SQLAlchemy recognizes it

↓

Can create a PostgreSQL table

Base tells SQLAlchemy that this Python class is a database model.






users
---------------------------------------------------------
id
- Integer
- Primary Key
- Unique
- Auto Increment
- Not Null

first_name
- String
- Not Null

last_name
- String
- Not Null

email
- String
- Unique
- Indexed
- Not Null

hashed_password
- String
- Not Null

is_active
- Boolean
- Default True
- Not Null

created_at
- DateTime
- Default Current Timestamp
- Not Null

updated_at
- DateTime
- Default Current Timestamp
- Auto Update on Modification
- Not Null