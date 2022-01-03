from tkinter import *
from dbAgence import*
from voiture import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb  
class GestionVoiture():
    def __init__(self,root): 
        self.root = root
        self.root.title("Gestion Voiture")  
        self.root.geometry("1000x2000")
        root.config(bg='SteelBlue')
        '''bg = PhotoImage(file = "voiture.png")
        
        # Create Canvas
        canvas1 = Canvas( root, width = 400,
                        height = 400)
        canvas1.pack(fill = "both", expand = True)
        # Display image
        canvas1.create_image( 0, 0, image = bg, 
                            anchor = "nw")'''
        self.matricule=StringVar()
        self.modele=StringVar()
        self.marque=StringVar()
        self.typeVoiture=StringVar()
        self.nbrPlace=StringVar()
        self.nbrPorte=StringVar()
        self.nbrCylindre=StringVar()
        self.energie=StringVar()
        self.puissance=StringVar()
        self.boiteVitesse=StringVar()
        self.prix=StringVar()
        self.nbrKilometrage=StringVar()
        self.idSearch=StringVar()
        #********************label*****************************************************   
        #============== matricule TEXTFIELD AND LABEL
        lblMat = Label(self.root, text="Matricule", font=("Helvetica", 16), fg="green")
        lblMat.grid(row = 1,column = 0,padx = 40,pady = 40)
        lblMat_field = Entry(self.root,textvariable = self.matricule)
        lblMat_field.grid(row = 1,column = 1,ipady = 7,ipadx = 5,padx = 5)
        #==============modele TEXTFIELD AND LABEL
        lblMod = Label(self.root, text="Modele:", font=("Helvetica", 10),  fg="green")  
        lblMod.grid(row = 1,column = 2,padx = 40,pady = 40)
        lblMod_field = Entry(self.root,textvariable = self.modele)
        lblMod_field.grid(row = 1,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #=======================marque LABEL AND TEXTFIELD
        lblmarque = Label(self.root, text="Marque:", font=("Helvetica", 10), fg="green")
        lblmarque.grid(row = 1,column = 4,pady = 40)
        lblmarque_field = Entry(self.root,textvariable = self.marque)
        lblmarque_field.grid(row = 1,column = 5,ipady = 7,ipadx = 20,padx = 20)
        #=======================Type voiture LABEL AND TEXTFIELD
        lblType = Label(self.root, text="Type:", font=("Helvetica", 10), fg="green")
        lblType.grid(row = 2,column = 0,pady = 40)
        lblType_field = Entry(self.root,textvariable = self.typeVoiture)
        lblType_field.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #======================nombre de place LABEL AND TEXTFIELD
        lblNbrPl = Label(self.root, text="Nombre de place:", font=("Helvetica", 10), fg="green")  
        lblNbrPl.grid(row = 2,column = 2,pady = 40)
        lblNbrPl_field = Entry(self.root,textvariable = self.nbrPlace)
        lblNbrPl_field.grid(row = 2,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #======================nombre de porte LABEL AND TEXTFIELD
        lblNbrPorte = Label(self.root, text="Nombre de porte:", font=("Helvetica", 10), fg="green")    
        lblNbrPorte.grid(row = 2,column =4 ,pady = 40)
        lblNbrPorte_field = Entry(self.root,textvariable = self.nbrPorte)
        lblNbrPorte_field.grid(row = 2,column = 5,ipady = 7,ipadx = 20,padx = 20)
        #======================nombre de cylindre LABEL AND TEXTFIELD
        lblCylind = Label(self.root, text="Nombre de cylindre", font=("Helvetica", 10),  fg="green")     
        lblCylind.grid(row = 3,column = 0,pady = 40)
        lblCylind_field = Entry(self.root,textvariable = self.nbrCylindre)
        lblCylind_field.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #======================energie LABEL AND TEXTFIELD
        lblEnerg = Label(self.root, text="Energie:", font=("Helvetica", 10),  fg="green")     
        lblEnerg.grid(row = 3,column = 2,pady = 40)
        lblEnerg_field = Entry(self.root,textvariable = self.energie)
        lblEnerg_field.grid(row = 3,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #======================puissance LABEL AND TEXTFIELD
        lblPuiss = Label(self.root, text="Puissance", font=("Helvetica", 10), fg="green") 
        lblPuiss.grid(row = 3,column = 4,pady = 40)
        lblPuiss_field = Entry(self.root,textvariable = self.puissance)
        lblPuiss_field.grid(row = 3,column = 5,ipady = 7,ipadx = 20,padx = 20)
        #======================boite vitesse LABEL AND TEXTFIELD
        lblBtVit = Label(self.root, text="Type de boite vitesse:",font=("Helvetica", 10),  fg="green")       
        lblBtVit.grid(row = 4,column = 0,pady = 40)
        lblBtVit_field = Entry(self.root,textvariable = self.boiteVitesse)
        lblBtVit_field.grid(row = 4,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #======================prix LABEL AND TEXTFIELD
        lblPrix = Label(self.root, text="Prix:", font=("Helvetica", 10),  fg="green")     
        lblPrix.grid(row = 4,column = 2,pady = 40)
        lblPrix_field = Entry(self.root,textvariable = self.prix)
        lblPrix_field.grid(row = 4,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #======================nombre de kilometrage LABEL AND TEXTFIELD
        lblNbrKilo = Label(self.root, text="Nombre de kilométrage", font=("Helvetica", 10),  fg="green")     
        lblNbrKilo.grid(row = 4,column = 4,pady = 40)
        lblNbrKilo_field = Entry(self.root,textvariable = self.nbrKilometrage)
        lblNbrKilo_field.grid(row = 4,column = 5,ipady = 7,ipadx = 20,padx = 20)
        #=======================Boutton ajouter
        ajout_etudiant_btn=Button(self.root,text="Ajouter",command=self.add,anchor='w')
        ajout_etudiant_btn.grid(row=5,column=1,ipady=4,ipadx=13,pady=40)
         #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        affich_etudiant_btn = Button(self.root,text = "Afficher",command = self.view,anchor='c')
        affich_etudiant_btn.grid(row = 5,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_etudiant_btn = Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        supp_etudiant_btn.grid(row = 5,column = 3,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        supp_etudiant_btn = Button(self.root,text = "Modifier",command = self.update,anchor='c')
        supp_etudiant_btn.grid(row = 5,column = 4,ipady = 4,ipadx = 13,pady = 40)
        #======================Boutton exit
        btn_exit = Button(self.root, text="Exit", fg="blue",command=self.exit)
        btn_exit.grid(row = 5,column = 5,ipady = 4,ipadx = 13,pady = 40)
        #======================Cherhcer label et boutton
        entSearch = Entry(self.root,textvariable=self.idSearch)  
        entSearch.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
        btn_search = Button(self.root, text="Chercher",command=self.search,anchor='c') 
        btn_search.grid(row = 6,column = 3,ipady = 4,ipadx = 13,pady = 40)
        '''columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7","#8","#9","#10","#11","#12")  
        self.tvStudent= ttk.Treeview(self.root,show="headings",height="5", columns=columns)  
        self.tvStudent.heading('#1', text='Matricule', anchor='center')  
        self.tvStudent.column('#1', width=60, anchor='center', stretch=False)  
        self.tvStudent.heading('#2', text='Modele', anchor='center')  
        self.tvStudent.column('#2', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#3', text='Marque', anchor='center')  
        self.tvStudent.column('#3',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#4', text='TypeVoiture', anchor='center')  
        self.tvStudent.column('#4',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#5', text='nbrPlace', anchor='center')  
        self.tvStudent.column('#5',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#6', text='NbrPorte', anchor='center')  
        self.tvStudent.column('#6', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#7', text='NbrCylindre', anchor='center')  
        self.tvStudent.column('#7', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#8', text='Energie', anchor='center')  
        self.tvStudent.column('#8', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#9', text='Puissance', anchor='center')  
        self.tvStudent.column('#9', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#10', text='typeBoiteVitesse', anchor='center')  
        self.tvStudent.column('#10', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#11', text='Prix', anchor='center')  
        self.tvStudent.column('#11', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#12', text='NbrKilometrage', anchor='center')  
        self.tvStudent.column('#12', width=10, anchor='center', stretch=True)   
'''        
    #fonction ajouter 
    def add(self):
       voit=Voiture(self.matricule.get(),self.modele.get(),self.marque.get(),self.typeVoiture.get(),int(self.nbrPlace.get()),int(self.nbrPorte.get()),int(self.nbrCylindre.get()),self.energie.get(),int(self.puissance.get()),self.boiteVitesse.get(),float(self.prix.get()),int(self.nbrKilometrage.get()))
       print("Voiture: ",voit.matricule)
       voit.ajouterVoiture()
       mb.showinfo("Info","ajoutation validé")
    def view(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('1000x1000')
        self.root.title("Gestion des voitures)")
        show_frame = Frame(self.root)
        show_frame.place(width = 1500,x = 0,y = 0 ,height = 800)
        labl_show = Label(show_frame,text = "Affichage des voitures")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 2000,height = 600,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5","6","7","8","9","10","11","12")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.column('7',width=80)
        tree.column('8',width=80)
        tree.column('9',width=80)
        tree.column('10',width=80)
        tree.column('11',width=80)
        tree.column('12',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "matricule",anchor='c')
        tree.heading("2",text = "modele",anchor='w')
        tree.heading("3",text = "marque",anchor='w')
        tree.heading("4",text="typeVoiture",anchor='w')
        tree.heading("5",text="nbrPlace",anchor='w')
        tree.heading("6",text="nbrPorte",anchor='w')
        tree.heading("7",text="nbrCylindre",anchor='w')
        tree.heading("8",text="energie",anchor='w')
        tree.heading("9",text="puissance",anchor='w')
        tree.heading("10",text="boiteVitesse",anchor='w')
        tree.heading("11",text="prix",anchor='w')
        tree.heading("12",text="nbrKilometrage",anchor='w')
        v=Voiture()
        rows=v.afficherVoiture()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}',f'{i[6]}',f'{i[7]}',f'{i[8]}',f'{i[9]}',f'{i[10]}',f'{i[11]}'))
            j+=1

    #Fonction de suppression d'une voiture sera appelée dans le boutton "Supprimer"  
    def remove(self):
        v = Voiture()
        v.supprimerVoiture(self.matricule.get())
        mb.showinfo("Info","suppression validé")
    #Fonction de modification d"un étudiant sera appelée dans le boutton "modifier"
    def update(self):
        #voit=Voiture(self.matricule,self.modele.get(),self.marque.get(),self.typeVoiture.get(),int(self.nbrPlace.get()),int(self.nbrPorte.get()),int(self.nbrCylindre.get()),self.energie.get(),int(self.puissance.get()),self.boiteVitesse.get(),float(self.prix.get()),int(self.nbrKilometrage.get()))
        voit=Voiture()

        voit.modifierVoiture(self.matricule.get(),self.modele.get(),self.marque.get(),self.typeVoiture.get(),int(self.nbrPlace.get()),int(self.nbrPorte.get()),int(self.nbrCylindre.get()),self.energie.get(),int(self.puissance.get()),self.boiteVitesse.get(),float(self.prix.get()),int(self.nbrKilometrage.get()))
        mb.showinfo("Info","modification validé")
    def exit(self):  
        MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
        if MsgBox == 'yes':  
            root.destroy()  
    def search(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('1000x1000')
        self.root.title("Gestion des voitures)")
        show_frame = Frame(self.root)
        show_frame.place(width = 1500,x = 0,y = 0 ,height = 800)
        labl_show = Label(show_frame,text = "Affichage des voitures")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 2000,height = 600,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5","6","7","8","9","10","11","12")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.column('7',width=80)
        tree.column('8',width=80)
        tree.column('9',width=80)
        tree.column('10',width=80)
        tree.column('11',width=80)
        tree.column('12',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "matricule",anchor='c')
        tree.heading("2",text = "modele",anchor='w')
        tree.heading("3",text = "marque",anchor='w')
        tree.heading("4",text="typeVoiture",anchor='w')
        tree.heading("5",text="nbrPlace",anchor='w')
        tree.heading("6",text="nbrPorte",anchor='w')
        tree.heading("7",text="nbrCylindre",anchor='w')
        tree.heading("8",text="energie",anchor='w')
        tree.heading("9",text="puissance",anchor='w')
        tree.heading("10",text="boiteVitesse",anchor='w')
        tree.heading("11",text="prix",anchor='w')
        tree.heading("12",text="nbrKilometrage",anchor='w')
        v=Voiture()
        rows=v.cherhcerVoiture(self.idSearch.get())
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}',f'{i[6]}',f'{i[7]}',f'{i[8]}',f'{i[9]}',f'{i[10]}',f'{i[11]}'))
            j+=1

    
root=Tk()
l=GestionVoiture(root)
root.mainloop()