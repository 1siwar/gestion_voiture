from tkinter import *
from dbAgence import*
from fournisseur import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb  
from PIL import ImageTk, Image
class GestionFournisseur():
    def __init__(self,root): 
        self.root = root
        self.root.title("Gestion Fournisseur")  
        self.root.geometry("1000x2000")
        #root.config(bg='SteelBlue')
        #bg = ImageTk.PhotoImage(file = "voiture.png")
        '''
        # Create Canvas
        canvas1 = Canvas( root, width = 400,
                        height = 400)
        canvas1.pack(fill = "both", expand = True)
        # Display image
        canvas1.create_image( 0, 0, image = bg, 
                            anchor = "nw")'''
        self.idFour=StringVar()
        self.nomFour=StringVar()
        self.prenomFour=StringVar()
        self.adresseFour=StringVar()
        self.email=StringVar()
        self.numTel=StringVar()
        self.idSearch=StringVar()
        #********************label*****************************************************   
        #============== id Fournisseur TEXTFIELD AND LABEL
        lblId = Label(self.root, text="Id", font=("Helvetica", 16), fg="green")
        lblId.grid(row = 1,column = 0,padx = 40,pady = 40)
        lblId_field = Entry(self.root,textvariable = self.idFour)
        lblId_field.grid(row = 1,column = 1,ipady = 7,ipadx = 5,padx = 5)
        #==============nom  TEXTFIELD AND LABEL
        lblNom = Label(self.root, text="Nom:", font=("Helvetica", 10),  fg="green")  
        lblNom.grid(row = 1,column = 2,padx = 40,pady = 40)
        lblNom_field = Entry(self.root,textvariable = self.nomFour)
        lblNom_field.grid(row = 1,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #=======================prenom LABEL AND TEXTFIELD
        lblPrenom = Label(self.root, text="Prenom:", font=("Helvetica", 10), fg="green")
        lblPrenom.grid(row = 1,column = 4,pady = 40)
        lblPrenom_field = Entry(self.root,textvariable = self.prenomFour)
        lblPrenom_field.grid(row = 1,column = 5,ipady = 7,ipadx = 20,padx = 20)
        #=======================adresse LABEL AND TEXTFIELD
        lblAdd = Label(self.root, text="addresse:", font=("Helvetica", 10), fg="green")
        lblAdd.grid(row = 2,column = 0,pady = 40)
        lblAdd_field = Entry(self.root,textvariable = self.adresseFour)
        lblAdd_field.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #======================email LABEL AND TEXTFIELD
        lblEmail = Label(self.root, text="email:", font=("Helvetica", 10), fg="green")  
        lblEmail.grid(row = 2,column = 2,pady = 40)
        lblEmail_field = Entry(self.root,textvariable = self.email)
        lblEmail_field.grid(row = 2,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #======================num Tel LABEL AND TEXTFIELD
        lblNumTel = Label(self.root, text="Num Tel:", font=("Helvetica", 10), fg="green")    
        lblNumTel.grid(row = 2,column =4 ,pady = 40)
        lblNumTel_field = Entry(self.root,textvariable = self.numTel)
        lblNumTel_field.grid(row = 2,column = 5,ipady = 7,ipadx = 20,padx = 20)
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=Button(self.root,text="Ajouter",command=self.add,anchor='w')
        ajout_Fournisseur_btn.grid(row=5,column=1,ipady=4,ipadx=13,pady=40)
         #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        affich_Fournisseur_btn = Button(self.root,text = "Afficher",command = self.view,anchor='c')
        affich_Fournisseur_btn.grid(row = 5,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        supp_Fournisseur_btn.grid(row = 5,column = 3,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier à ajouter après boutton "modifier" dans __init()__
        supp_Fournisseur_btn = Button(self.root,text = "Modifier",command = self.update,anchor='c')
        supp_Fournisseur_btn.grid(row = 5,column = 4,ipady = 4,ipadx = 13,pady = 40)
        #======================Boutton exit
        btn_exit = Button(self.root, text="Quitter", fg="blue",command=self.exit)
        btn_exit.grid(row = 5,column = 5,ipady = 4,ipadx = 13,pady = 40)
        #======================Cherhcer label et boutton
        entSearch = Entry(self.root,textvariable=self.idSearch)  
        entSearch.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
        btn_search = Button(self.root, text="Chercher",command=self.search,anchor='c') 
        btn_search.grid(row = 6,column = 3,ipady = 4,ipadx = 13,pady = 40)
    #fonction ajouter 
    def add(self):
       four=Fournisseur(self.idFour.get(),self.nomFour.get(),self.prenomFour.get(),self.adresseFour.get(),self.email.get(),int(self.numTel.get()))
       print("Voiture: ",four.idFour)
       four.ajouterFournisseur()
       mb.showinfo("Info","ajoutation validé")
    def view(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des Fournisseurs")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des Fournisseurs")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 600,height = 300,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "idFour",anchor='c')
        tree.heading("2",text = "nomFour",anchor='w')
        tree.heading("3",text = "prenomFour",anchor='w')
        tree.heading("4",text="adresseFour",anchor='w')
        tree.heading("5",text="emailFour",anchor='w')
        tree.heading("6",text="numTelfour",anchor='w')
        f=Fournisseur()
        rows=f.afficherFournisseur()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1

    #Fonction de suppression d'un fournisseur sera appelée dans le boutton "Supprimer"  
    def remove(self):
        f = Fournisseur()
        f.supprimerFournisseur(self.idFour.get())
        mb.showinfo("Info","suppression validé")
    #Fonction de modification d"un fournisseur sera appelée dans le boutton "modifier"
    def update(self):
        four=Fournisseur()
        four.modifierFournisseur(self.idFour.get(),self.nomFour.get(),self.prenomFour.get(),self.adresseFour.get(),self.email.get(),int(self.numTel.get()))
        mb.showinfo("Info","modification validé")
    def exit(self):  
        MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
        if MsgBox == 'yes':  
            root.destroy()  
    def search(self):
        #self.root.title("Fournisseur Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des Fournisseurs")
        show_frame = Frame(self.root)
        show_frame.place(width = 800,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage d'un fournisseur")
        labl_show.pack()
        #========================Main Frame
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 600,height = 300,x = 8,y = 58)
        tree = ttk.Treeview(main_frame,height = 200)
        vsb = ttk.Scrollbar(main_frame,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=50)
        tree.column('1',width=80)
        tree.column('2',width=80)
        tree.column('3',width=80)
        tree.column('4',width=80)
        tree.column('5',width=80)
        tree.column('6',width=80)
        tree.heading("#0",text = "Num",anchor='c')
        tree.heading("1",text = "idFour",anchor='c')
        tree.heading("2",text = "nomFour",anchor='w')
        tree.heading("3",text = "prenomFour",anchor='w')
        tree.heading("4",text="adresseFour",anchor='w')
        tree.heading("5",text="emailFour",anchor='w')
        tree.heading("6",text="numTelfour",anchor='w')
        f=Fournisseur()
        rows=f.chercherFournisseur(self.idSearch.get())
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1

    
root=Tk()
l=GestionFournisseur(root)
root.mainloop()