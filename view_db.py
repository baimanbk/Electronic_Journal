import sqlite3

# Connect to the database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Function to print all tables
def print_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(f"Table: {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]});")
        columns = cursor.fetchall()
        for column in columns:
            print(f"Column: {column[1]} - {column[2]}")
        cursor.execute(f"SELECT * FROM {table[0]};")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()

# Print all tables and their contents
print_tables()

# Close the connection
conn.close()
