import sqlite3

conn = sqlite3.connect("myDB.db")
cur = conn.cursor() #methode permettant de communiquer avec la base de donnes avec la requete sql

req = "select * from student"
result = cur.execute(req)

for row in result :
    print("ID :", row[0])
    print("Nom :", row[1])
    print("Email :", row[2])
    print("Age:", row[3])