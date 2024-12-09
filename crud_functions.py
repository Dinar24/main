import sqlite3


def initiate_db():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()

    connection.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL 
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    initiate_db()
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products
