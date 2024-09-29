import sqlite3

conn = sqlite3.connect('viber_users.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    user_id TEXT PRIMARY KEY,
    number TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL CHECK (is_admin IN (0, 1))
)
''')

conn.commit()
conn.close()

print("Database and table created successfully.")
