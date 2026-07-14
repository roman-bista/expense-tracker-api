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