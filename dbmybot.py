import sqlite3
from datetime import datetime
connection = sqlite3.connect("dzbot")
sql = connection.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, name TEXT, phone TEXT, reg_data DATETIME);")

def add_user(user_id, name, phone):
    connection = sqlite3.connect("dzbot")
    sql = connection.cursor()
    sql.execute("INSERT INTO users(user_id, name, phone, reg_data) (?,?,?,?);", (user_id, name, phone, datetime.now()))
    connection.commit()
    print("Данные сохранены!")
def check_user(user_id):
    connection = sqlite3.connect("dzbot")
    sql = connection.cursor()
    checker = sql.execute("SELECT user_id FROM users WHERE user_id=?;", (user_id,)).fetchone()
    if checker:
        return True
    return False

