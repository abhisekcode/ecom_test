import sqlite3
from datetime import datetime

def insert_product(product_name):
    conn = sqlite3.connect("ecom.db")
    cursor = conn.cursor()

    cursor.execute(
    "INSERT INTO cart (product_name, created_at) VALUES (?, ?)",
    (product_name, datetime.now().isoformat())
)
    
    conn.commit()
    conn.close()

def clear_cart():
    conn = sqlite3.connect("ecom.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cart")

    conn.commit()
    conn.close()


def get_products():
    conn = sqlite3.connect("ecom.db")
    cursor = conn.cursor()

    cursor.execute("SELECT product_name FROM cart")
    data = cursor.fetchall()

    conn.close()

    return [d[0] for d in data]