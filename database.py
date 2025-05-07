import sqlite3 # Built-in module to interact with SQLite database

# SQL statement to create the 'beans' table if it doesn't exist
CREATE_BEANS_TABLE = """
CREATE TABLE IF NOT EXISTS beans (
    id INTEGER PRIMARY KEY, 
    name TEXT, 
    method TEXT, 
    rating INTEGER
    );
"""

# SQL statement for inserting and querying data
INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?, ?, ?);"
GET_ALL_BEANS = "SELECT * FROM beans;"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"
GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
WHERE LOWER(name) = LOWER(?)
ORDER BY rating DESC
LIMIT 1;
"""

# Connect to the database (creates data.db if it doesn't exist)
def connect():
    return sqlite3.connect("data.db")

# Create the beans table
def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

# Insert a new bean into the table
def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))

# Retrieve all bean records
def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()

# Retrieve beans filtered by name
def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()

# Retrieve the top-rated preparation method for a specific bean name
def get_best_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()