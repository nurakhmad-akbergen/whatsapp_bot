import sqlite3

def init_db():
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT,
        product TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_order(phone, product):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders (phone, product) VALUES (?, ?)",
        (phone, product)
    )

    conn.commit()
    conn.close()
