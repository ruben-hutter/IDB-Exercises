import sqlite3
import csv

conn = sqlite3.connect('example.db')

# drop existing tables if they exist
conn.execute('DROP TABLE IF EXISTS names;')
conn.execute('DROP TABLE IF EXISTS counts;')

conn.execute("PRAGMA foreign_keys=on;")

conn.execute('''
     CREATE TABLE IF NOT EXISTS names (
         id INTEGER PRIMARY KEY,
         name TEXT NOT NULL UNIQUE CHECK(length(name) > 0)
     );
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS counts (
        id INTEGER,
        date DATE,
        count INTEGER CHECK(count > 0),
        PRIMARY KEY (id, date),
        FOREIGN KEY (id) REFERENCES names(id)
    );
''')

conn.commit()

with open('100127.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    next(csvreader) # skip header row

    for row in csvreader:
        try:
            conn.execute(
                'INSERT OR IGNORE INTO names (name) VALUES (?);',
                (row[1],)
            )

            result = conn.execute(
                'SELECT id FROM names WHERE name = ?;',
                (row[1],)
            )
            id = result.fetchone()[0] if result else None

            conn.execute(
                'INSERT INTO counts (id, date, count) VALUES (?, ?, ?);',
                (id, row[0], row[2])
            )
        except Exception as e:
            print(f"Error inserting values: {row[0]}, {row[1]}, {row[2]}")
            print(f"Error message: {e}")
            break

conn.commit()
conn.close()
