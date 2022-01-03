import mysql.connector
#fonction qui permet de connecter à la base de donnée agencelocation dans mysql avec le user et le password
def connect_BD():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="agencelocation"
    )
    return mydb

db=connect_BD()
mycursor=db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS LOCATION(id_l int PRIMARY KEY,description VARCHAR(255),date_debut VARCHAR(255) ,date_fin VARCHAR(255) , prix_loc FLOAT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS FACTURE(id_f int PRIMARY KEY,id_l int,prix_fact FLOAT , date_fact VARCHAR(255) , date_pai VARCHAR(255))")
#creation de la table voiture dans la base agencelocation
mycursor.execute("CREATE TABLE IF NOT EXISTS PANNE2(id_p INT(10) PRIMARY KEY, id_l INT(20), matricule INT(20), type_panne VARCHAR(20),cout INT(20))")
mycursor.execute("CREATE TABLE IF NOT EXISTS VOITURE(matricule VARCHAR(255) PRIMARY KEY, modele VARCHAR(255), typeVoiture VARCHAR(255), nbrPlace INT,prix FLOAT, quantite INT)")
#creation de la table fournisseur dans la base agencelocation
mycursor.execute("CREATE TABLE IF NOT EXISTS Fournisseur(idFour VARCHAR(255) PRIMARY KEY, nomFour VARCHAR(255), adresseFour VARCHAR(255), emailFour VARCHAR(255), numTelFour INT,matricule VARCHAR(255), FOREIGN KEY (matricule) REFERENCES VOITURE(matricule))")
#mycursor.execute("CREATE TABLE IF NOT EXISTS Fournisseur(idFour VARCHAR(255) PRIMARY KEY, nomFour VARCHAR(255),prenomFour VARCHAR(255), adresseFour VARCHAR(255), emailFour VARCHAR(255), numTelFour INT)")
#afficher les tables de la base agenceLocation
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)