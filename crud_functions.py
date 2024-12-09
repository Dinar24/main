import sqlite3
import asyncio

connection = sqlite3.connect('product_data.db')
cursor= connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT,
    description TEXT,
    price INT
    )
    '''),
    connection.commit()

initiate_db()

# вариант 1
def get_all_products():
    connection = sqlite3.connect('product_data.db')
    cursor = connection.cursor()
    products=cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    return products


connection.commit()
connection.close()