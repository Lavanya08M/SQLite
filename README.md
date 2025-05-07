# SQLite
Python project that uses SQLite database to Store data.

# Coffee Bean Rating App

A simple Python terminal application to help users record and track their coffee bean preferences based on preparation methods and ratings. Data is stored in a local SQLite database (`data.db`).

## Features

- Add a new coffee bean with preparation method and rating.
- View all beans saved in the database.
- Search for beans by name.
- Find the best-rated preparation method for a specific bean.

## File Structure

- `app.py`: Main application that interacts with the user.
- `database.py`: Handles all database operations (creation, insertion, queries).
- `data.db`: SQLite database file (created automatically when the app is run).

## Requirements

- Python 3.x (preferably Python 3.7 or later)
- No external libraries needed (uses built-in `sqlite3`)
