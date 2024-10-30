import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Id, Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s, %s)"

val = [
  (1, 'Luna','Labrador Retriever', 30, 5),
  (2, 'Felix','Gatto Europeo', 4, 3),
  (3, 'Rocky','Pastore Tedesco', 35, 6),
  (4, 'Blu','Pappagallo Ara', 1, 8),
  (5, 'Spike','Porcellino d India', 1, 2),
]

mycursor.executemany(sql, val)

mydb.commit()

#mycursor.execute("SELECT * FROM Mammiferi")

#myresult = mycursor.fetchall()

#for x in myresult:
 # print(x)
