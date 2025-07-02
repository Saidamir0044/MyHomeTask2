# Ex1
import sqlite3

conn = sqlite3.connect("mydata.db")
cur = conn.cursor()
cur.execute("CREATE TABLE Roster (Name TEXT, Species TEXT, Age integer")
conn.commit()
conn.close()

# Ex2
import sqlite3

conn = sqlite3.connect("mydata.db")
cur = conn.cursor()
cur.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", ("Benjamin Sisko", "Human", 40))
cur.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", ("Jadzia Dax", "Trill", 300))
cur.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", ("Kira Nerys", "Bajoran", 29))
conn.commit()
conn.close()

#Ex3
import sqlite3

conn = sqlite3.connect("mydata.db")
cur = conn.cursor()

cur.execute("Update Roster SET Name = ? WHERE Name = ?",("Ezri Dax", "Jadzia Dax" ))
conn.commit()
conn.close()

# Ex4
import sqlite3

conn = sqlite3.connect("mydata.db")
cur = conn.cursor()

cur.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
