#importer le module db 
from dbAgence import*
class Voiture:
    #appele de la connexion de la base
    db=connect_BD()
    mycursor=db.cursor()
    #initialisation de les attributs d'une voiture
    def __init__(self,matricule="",modele="",typeVoiture="",nbrPlace=0,prix=0,quantite=0):
        self.matricule=matricule
        self.modele=modele
        self.typeVoiture=typeVoiture
        self.nbrPlace=nbrPlace
        self.prix=prix
        self.quantite=quantite
    
    #fonction permet d'insérer les attributs d'une voiture dans la table voiture
    def ajouterVoiture(self):

        sql="INSERT INTO voiture(matricule,modele,typeVoiture,nbrPlace,prix,quantite) VALUES (%s,%s,%s,%s,%s,%s)"
        val=(self.matricule,self.modele,self.typeVoiture,self.nbrPlace,self.prix,self.quantite)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"record inserted.")
    #fonction permet d'afficher tous les attributs de la table voiture
    def afficherVoiture(self):
        self.mycursor.execute('SELECT * FROM voiture')
        result=self.mycursor.fetchall()
        return result
    #fonction permet de supprimer une voiture selon leur matricule
    def supprimerVoiture(self,mat):
        sql="DELETE FROM voiture WHERE matricule = %s"
        val=(mat,)
        self.mycursor.execute(sql,val)
        self.db.commit()
    #fonction permet de modifier le nom d'un etudiant selon leur numéro d'inscrit
    def modifierVoiture(self,mat,modele,marque,typeVoiture,prix,quantite):
        sql="UPDATE voiture SET modele=%s, typeVoiture=%s,nbrPlace=%s,prix=%s,quantite=%s WHERE matricule=%s"
        val=(modele,marque,typeVoiture,prix,quantite,mat)
        self.mycursor.execute(sql,val)
        self.db.commit()
    def chercherVoiture(self,mat):
        sql='SELECT * FROM voiture WHERE matricule= %s'
        val=(mat,)
        self.mycursor.execute(sql,val)
        result=self.mycursor.fetchall()
        return result
    def QuantiteVoiture(self):
        sql='SELECT quantite FROM voiture '
        
        self.mycursor.execute(sql)
        result=self.mycursor.fetchall()
        return result
    def ModeleVoiture(self):
        sql='SELECT modele FROM voiture '
        
        self.mycursor.execute(sql)
        result=self.mycursor.fetchall()
        return result
    def ModQte(self):
        sql='SELECT modele,quantite FROM voiture '
        
        self.mycursor.execute(sql)
        result=self.mycursor.fetchall()
        return result

