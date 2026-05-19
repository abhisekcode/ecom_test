import sqlite3

conn = sqlite3.connect("ecom.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE cart (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    created_at TEXT
)
""")

conn.commit()
conn.close()

print("DB recreated")