import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(create_table)



user = (1, 'arup', 'asdfg')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'jeet', '123'),
    (3, 'soma', 'xyz'),
    (4, 'raj', 'pqr')

]
cursor.executemany(insert_query, users)


select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)


#Committing changes to the DB and closing the connection
connection.commit()
connection.close()
