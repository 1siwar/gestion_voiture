#importer le module db 
from dbAgence import*
from voiture import*
class Fournisseur :
    #appele de la connexion de la base
    db=connect_BD()
    mycursor=db.cursor()
    #initialisation de les attributs d'un fournisseur
    def __init__(self,idFour="",nomFour="",prenomFour="",adresseFour="",emailFour="",numTelFour=0):
        self.idFour=idFour
        self.nomFour=nomFour
        self.prenomFour=prenomFour
        self.adresseFour=adresseFour
        self.emailFour=emailFour
        self.numTelFour=numTelFour
    #fonction permet d'insérer les attributs d'un fournisseur dans la table fournisseur
    def ajouterFournisseur(self):
        sql="INSERT INTO fournisseur(idFour,nomFour,prenomFour,adresseFour,emailFour,numTelFour) VALUES (%s,%s,%s,%s,%s,%s)"
        val=(self.idFour,self.nomFour,self.prenomFour,self.adresseFour,self.emailFour,self.numTelFour)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"record inserted.")
    #fonction permet d'afficher tous les attributs de la table fournisseur
    def afficherFournisseur(self):
        self.mycursor.execute('SELECT * FROM fournisseur')
        result=self.mycursor.fetchall()
        return result
    #fonction permet de supprimer un fournisseur selon leur id
    def supprimerFournisseur(self,idF):
        sql="DELETE FROM fournisseur WHERE idFour = %s"
        val=(idF,)
        self.mycursor.execute(sql,val)
        print(self.mycursor.rowcount,"record deleted.")
        self.db.commit()
    #fonction permet de modifier les attributs d'un fournisseur
    def modifierFournisseur(self,idf,nom,prenom,add,email,num):
        sql="UPDATE fournisseur SET nomFour=%s, prenomFour=%s,adresseFour=%s, emailFour=%s, numTelFour=  %s WHERE idFour=%s"
        val=(nom,prenom,add,email,num,idf)
        self.mycursor.execute(sql,val)
        print(self.mycursor.rowcount,"record updated.")
        self.db.commit()
    def chercherFournisseur(self,idF):
        sql='SELECT * FROM fournisseur WHERE idFour= %s'
        val=(idF,)
        self.mycursor.execute(sql,val)
        result=self.mycursor.fetchall()
        return result