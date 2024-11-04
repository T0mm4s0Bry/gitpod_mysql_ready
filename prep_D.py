import mysql.connector
import prep_C
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)
mycursor = mydb.cursor()
i=0
for i in range(5):
    Nome_Proprio = input("Nome Proprio : ")
    Razza = input("Razza: ")
    Peso = input("Peso (in kg): ")
    Eta = input("Età (in anni): ")
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = (Nome_Proprio, Razza, Peso, Eta)
    mycursor.execute(sql, val)
    i=i+1
mydb.commit()
print(mycursor.rowcount, "animali inseriti.")
if i == 5:  
    prep_C.get_Mammiferi()