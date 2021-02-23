import sqlite3

con = sqlite3.connect('contact.db')
print('Database opened successfully')

con.execute('create table Contact (sno INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email VARCHAR NOT NULL, phone VARCHAR NOT NULL, message TEXT NOT NULL)')
print('Database created successfully')

con.close()