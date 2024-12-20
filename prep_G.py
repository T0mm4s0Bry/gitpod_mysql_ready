import mysql.connector


def connetti_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Animali"
    )
    
def inserisci_animale():
    Nome_Proprio = input("Nome Proprio: ")
    Razza = input("Razza: ")
    Peso = float(input("Peso (in kg): "))
    Eta = int(input("Età (in anni): "))

    mydb = connetti_database()
    cursor = mydb.cursor()
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = (Nome_Proprio, Razza, Peso, Eta)
    cursor.execute(sql, val)
    mydb.commit()
    print("Animale inserito con successo.")
    mydb.close()

def visualizza_animali():
    mydb = connetti_database()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Mammiferi")
    animali = cursor.fetchall()

    print("\nLista degli animali:")
    for animale in animali:
        print(f"ID: {animale[0]}, Nome Proprio: {animale[1]}, Razza: {animale[2]}, Peso: {animale[3]} kg, Età: {animale[4]} anni")
    mydb.close()
 
def elimina_animale():
    visualizza_animali()
    id_animale = int(input("\nInserisci l'ID dell'animale da eliminare: "))

    mydb = connetti_database()
    cursor = mydb.cursor()
    sql = "DELETE FROM Mammiferi WHERE id = %s"
    val = (id_animale,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Animale eliminato con successo.")
    mydb.close()

def modifica_animale():
    visualizza_animali()
    id_animale = int(input("\nInserisci l'ID dell'animale da modificare: "))

    Nome_Proprio = input("Nuovo Nome Proprio: ")
    Razza = input("Nuova Razza: ")
    Peso = float(input("Nuovo Peso (in kg): "))
    Eta = int(input("Nuova Età (in anni): "))

    mydb = connetti_database()
    cursor = mydb.cursor()
    sql = "UPDATE Mammiferi SET Nome_Proprio = %s, Razza = %s, Peso = %s, Eta = %s WHERE id = %s"
    val = (Nome_Proprio, Razza, Peso, Eta, id_animale)
    cursor.execute(sql, val)
    mydb.commit()
    print("Animale modificato con successo.")
    mydb.close()

def menu():
    while True:
        print("\n--- Menu Gestione Animali ---")
        print("Premi 1 per inserire un nuovo animale")
        print("Premi 2 per visualizzare tutti gli animali")
        print("Premi 3 per eliminare un animale")
        print("Premi 4 per modificare un animale")
        print("Premi 5 per uscire")

        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            inserisci_animale()
        elif scelta == '2':
            visualizza_animali()
        elif scelta == '3':
            elimina_animale()
        elif scelta == '4':
            modifica_animale()
        elif scelta == '5':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

# Avvia il menu
menu()
