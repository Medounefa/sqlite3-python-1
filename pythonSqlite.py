import sqlite3

conn = sqlite3.connect("myDB.db")
cur = conn.cursor() #methode permettant de communiquer avec la base de donnes avec la requete sql

adm = input("Entrer votre nom")
email = input("intrer votre email")
age = int(input("Entrer votre age"))
# req = "CREATE TABLE student(id integer primary key autoincrement, nom text, email text, age float)"
req = "insert into student (nom, email, age) values(?, ?, ?)"
cur.execute(req, (adm, email, age))
conn.commit() #permet d'emvoyer la requete
conn.close() #fermet la connection