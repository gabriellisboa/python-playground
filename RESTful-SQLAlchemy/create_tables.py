import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER  PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

insert_user = 'INSERT INTO users VALUES (1, "gabiroto", "senha")'
cursor.execute(insert_user)

connection.commit()
connection.close()

print("Success creating tables")