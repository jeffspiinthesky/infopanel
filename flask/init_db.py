import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

# cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('200','OK','TEST')")
# cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('500','FAIL','TEST2')")
connection.commit()
connection.close()