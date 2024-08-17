import sqlite3
import json
from pathlib import Path

# Load movie data from JSON file
movies = json.loads(Path("movies.json").read_text())

# Connect to SQLite database
with sqlite3.connect("db.sqlite") as conn:
    # Create the Movies table if it does not exist
    conn.execute("""
    CREATE TABLE IF NOT EXISTS Movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    """)

    # SQL command to insert data
    command = "INSERT INTO Movies (id, title, year) VALUES (?, ?, ?)"
    
    # Insert each movie into the database
    for movie in movies:
        # Convert the dictionary values to a tuple
        conn.execute(command, (movie['id'], movie['title'], movie['year']))
    
    # Commit the transaction
    conn.commit()
