try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
from tkinter import *
from dbAgence import*
from fournisseur import Fournisseur
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (IndexPage, PageOne, GestionFournisseur):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("IndexPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
class IndexPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Gestion des vehicule", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Gestion Voiture",bg='lightskyblue2', font=('Arial', 11, 'bold'),
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Gestion Fournisseur",bg='lightskyblue2', font=('Arial', 11, 'bold'),
                            command=lambda: controller.show_frame("GestionFournisseur"))
        button1.pack()
        button2.pack()
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Gestion Voiture", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Retour",
                           command=lambda: controller.show_frame("IndexPage"))
        button.pack()
'''class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Gestion Fournisseur", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Retour",
                           command=lambda: controller.show_frame("IndexPage"))
        button.pack()'''
class GestionFournisseur(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        self.root = controller
        self.root.title("Gestion Fournisseur")  
        self.root.geometry("1100x2000")
        #root.config(bg='SteelBlue')
        self.idFour=StringVar()
        self.nomFour=StringVar()
        self.prenomFour=StringVar()
        self.adresseFour=StringVar()
        self.email=StringVar()
        self.numTel=IntVar()
        self.idSearch=StringVar()
        self.idFourSupp=StringVar()
        self.controller = controller

        label = tk.Label(self, text="Gestion Fournisseur", font=controller.title_font)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Retour",
                           command=lambda: controller.show_frame("IndexPage"))
        #button.grid(row = 1, column = 1, padx = 10, pady = 10)
        button.pack()
        ajout_Fournisseur_btn=tk.Button(self,text="Ajouter Fournisseur",anchor='w',bg='palegreen2', font=('Arial', 11, 'bold'))
        #ajout_Fournisseur_btn.grid(row=0,column=0,ipady=4,ipadx=13,pady=40)
        ajout_Fournisseur_btn.grid_rowconfigure(2,weight=1)
        ajout_Fournisseur_btn.grid_columnconfigure(1,weight=1)
        #=====================Boutton Supprimer ?? ajouter apr??s boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = tk.Button(self,text = "Supprimer Fournisseur",anchor='c',bg='lightskyblue2', font=('Arial', 11, 'bold'))
        #supp_Fournisseur_btn.grid(row = 1,column = 0,ipady = 4,ipadx = 13,pady = 40)
        supp_Fournisseur_btn.pack()
        '''#===============================Affichage
        
        #=======================Boutton ajouter
        ajout_Fournisseur_btn=tk.Button(self.root,text="Ajouter Fournisseur",command=self.add,anchor='w',bg='palegreen2', font=('Arial', 11, 'bold'))
        ajout_Fournisseur_btn.grid(row=0,column=0,ipady=4,ipadx=13,pady=40)
        #=====================Boutton Supprimer ?? ajouter apr??s boutton "Afficher" dans __init()__
        supp_Fournisseur_btn = tk.Button(self.root,text = "Supprimer Fournisseur",command = self.remove,anchor='c',bg='lightskyblue2', font=('Arial', 11, 'bold'))
        supp_Fournisseur_btn.grid(row = 1,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton modifier ?? ajouter apr??s boutton "modifier" dans __init()__
        supp_Fournisseur_btn = Button(self.root,text = "Modifier Fournisseur",command = self.update,anchor='c',bg='palegreen2', font=('Arial', 11, 'bold'))
        supp_Fournisseur_btn.grid(row = 2,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #======================Cherhcer label et boutton
        #entSearch = Entry(self.root,textvariable=self.idSearch)  
        #entSearch.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
        btn_search = Button(self.root, text="Chercher Fournisseur",command=self.search,anchor='c',bg='palegreen2', font=('Arial', 11, 'bold')) 
        btn_search.grid(row = 3,column = 0,ipady = 4,ipadx = 13,pady = 40)
        #======================Boutton exit
        btn_exit = Button(self.root, text="Quitter",command=self.exit,bg='lightsteelblue2', font=('Arial', 11, 'bold'))
        btn_exit.grid(row = 4,column = 0,ipady = 4,ipadx = 13,pady = 40)
        
        #********************label*****************************************************   

        #============== id Fournisseur TEXTFIELD AND LABEL
        lblId = Label(self.root, text="Id", font=("Helvetica", 16), fg="green")
        lblId.grid(row = 0,column = 1,padx = 40,pady = 40)
        lblId_field = Entry(self.root,textvariable = self.idFour)
        lblId_field.grid(row = 0,column = 2,ipady = 7,ipadx = 5,padx = 5)
        #==============nom  TEXTFIELD AND LABEL
        lblNom = Label(self.root, text="Nom:", font=("Helvetica", 10),  fg="green")  
        lblNom.grid(row = 0,column = 3,padx = 40,pady = 40)
        lblNom_field = Entry(self.root,textvariable = self.nomFour)
        lblNom_field.grid(row = 0,column = 4,ipady = 7,ipadx = 20,padx = 20)
        #=======================prenom LABEL AND TEXTFIELD
        lblPrenom = Label(self.root, text="Prenom:", font=("Helvetica", 10), fg="green")
        lblPrenom.grid(row = 0,column = 5,pady = 40)
        lblPrenom_field = Entry(self.root,textvariable = self.prenomFour)
        lblPrenom_field.grid(row = 0,column = 6,ipady = 7,ipadx = 20,padx = 20)
        #=======================adresse LABEL AND TEXTFIELD
        lblAdd = Label(self.root, text="addresse:", font=("Helvetica", 10), fg="green")
        lblAdd.grid(row = 1,column = 1,pady = 40)
        lblAdd_field = Entry(self.root,textvariable = self.adresseFour)
        lblAdd_field.grid(row = 1,column = 2,ipady = 7,ipadx = 20,padx = 20)
        #======================email LABEL AND TEXTFIELD
        lblEmail = Label(self.root, text="email:", font=("Helvetica", 10), fg="green")  
        lblEmail.grid(row = 1,column = 3,pady = 40)
        lblEmail_field = Entry(self.root,textvariable = self.email)
        lblEmail_field.grid(row = 1,column = 4,ipady = 7,ipadx = 20,padx = 20)
        #======================num Tel LABEL AND TEXTFIELD
        lblNumTel = Label(self.root, text="Num Tel:", font=("Helvetica", 10), fg="green")    
        lblNumTel.grid(row = 1,column = 5,pady = 40)
        lblNumTel_field = Entry(self.root,textvariable = self.numTel)
        lblNumTel_field.grid(row = 1,column = 6,ipady = 7,ipadx = 20,padx = 20)
        #=========================Button=====================================================
        ajout_Fournisseur_btn=Button(self.root,text="Valider",command=self.ajouter,bg='palegreen2', font=('Arial', 11, 'bold'),anchor='w')
        ajout_Fournisseur_btn.grid(row=2,column=3,ipady=4,ipadx=13,pady=40)
        ajout_Fournisseur_btn=Button(self.root,text="Annuler",command=self.exit,bg='lightsteelblue2', font=('Arial', 11, 'bold'),anchor='w')
        ajout_Fournisseur_btn.grid(row=2,column=4,ipady=4,ipadx=13,pady=40)
        #========================Main Frame================================================
        main_frame = Frame(self.root,bd = 20,relief = SUNKEN)
        main_frame.place(width = 700,height = 500,x = 200,y = 400)
        tree = ttk.Treeview(main_frame,height = 100)
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

    #fonction ajouter 
    
    #def add(self):
        self.root=Tk()
        self.root.geometry('900x300')
        self.root.title("Gestion des Fournisseurs")
        
        
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
    #Fonction de suppression d'un fournisseur sera appel??e dans le boutton "Supprimer"  
    def remove(self):
        self.fenetre = root
        self.fenetre=Tk()
        self.fenetre.geometry('900x300')
        self.fenetre.title("Gestion des Fournisseurs")
         #============== id Fournisseur TEXTFIELD AND LABEL
        lblIdSupp = Label(self.fenetre, text="Id", font=("Helvetica", 16), fg="green")
        lblIdSupp.grid(row = 0,column = 1,padx = 40,pady = 40)
        lblIdSupp_field = Entry(self.fenetre,textvariable = self.idFourSupp)
        lblIdSupp_field.grid(row = 0,column = 2,ipady = 7,ipadx = 5,padx = 5)
         #=====================Boutton Supprimer ?? ajouter apr??s boutton "Afficher" dans __init()__
        supp_FournisseurId_btn = Button(self.fenetre,text = "Supprimer Fournisseur",command = self.supprimer,anchor='c',bg='lightskyblue2', font=('Arial', 11, 'bold'))
        supp_FournisseurId_btn.grid(row = 1,column = 0,ipady = 4,ipadx = 13,pady = 40)
    
        
    #Fonction de modification d"un fournisseur sera appel??e dans le boutton "modifier"
    def update(self):
        four=Fournisseur()
        four.modifierFournisseur(self.idFour.get(),self.nomFour.get(),self.prenomFour.get(),self.adresseFour.get(),self.email.get(),int(self.numTel.get()))
        mb.showinfo("Info","modification valid??")
    def exit(self):  
        MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
        if MsgBox == 'yes':  
            root.destroy()  
    def search(self):
        #self.root.title("Fournisseur Management(Details)")
        #==========================Show Frame================================
        self.root=Tk()
        self.root.geometry('700x300')
        self.root.title("Gestion des Fournisseurs")
        #===========================label 
        lblSearch = Label(self.root, text="Id", font=("Helvetica", 16), fg="green")
        lblSearch.grid(row = 0,column = 1,padx = 40,pady = 40)
        entSearch = Entry(self.root,textvariable=self.idSearch)  
        entSearch.grid(row = 0,column = 2,ipady = 4,ipadx = 13,pady = 40)
        btn_search = Button(self.root, text="Chercher Fournisseur",command=self.search,anchor='c',bg='palegreen2', font=('Arial', 11, 'bold')) 
        btn_search.grid(row = 3,column = 0,ipady = 4,ipadx = 13,pady = 40)
       #======================================================================
        show_frame = Frame(self.root)
        show_frame.place(width = 500,x = 200,y = 400 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage d'un fournisseur")
        labl_show.pack()
        #========================Main Frame=================================
        main_frame = Frame(self.root,bd = 10,relief = SUNKEN)
        main_frame.place(width = 600,height = 300,x = 200,y = 400)
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
    def ajouter(self):
        four=Fournisseur(self.idFour.get(),self.nomFour.get(),self.prenomFour.get(),self.adresseFour.get(),self.email.get(),self.numTel.get())
        print("Fournisseur: ",four.idFour)
        four.ajouterFournisseur()
        #mb.showinfo("Info","ajoutation valid??")
    def supprimer(self):
        f = Fournisseur()
        f.supprimerFournisseur(self.idFourSupp.get())
        mb.showinfo("Info","suppression valid??")
    
'''
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()



