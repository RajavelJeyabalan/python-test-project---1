import sqlite3

con = sqlite3.connect("K&N.db")

print("Database connected")

con.execute("Select * from fenroll")
con.execute("Select * from venroll")


print("table created")

con.close()

