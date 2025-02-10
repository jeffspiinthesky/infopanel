import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

# cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('200','OK','TEST')")
# cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('500','FAIL','TEST2')")
cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('200','OK: 152:0 154:0 155:0','Cameras')")
cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('200','OK','UK-Bridge')")
cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('200','OK: UUU','UK-RAID')")
cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('200','OK','UK-US')")
cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('200','OK: UUU','US-RAID')")
cursor.execute("INSERT INTO status (code, message, vpn) VALUES ('200','OK','US-UK')")

connection.commit()
connection.close()
