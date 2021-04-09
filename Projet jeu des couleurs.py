#Projet jeu des couleurs
#L1 MIASHS TD02
#Pentinat Antoine, Négrier Amélie, Tairou Iswat, Auclerc Emre, Huguen Marine, Rafiq Loubna

#création de la fenetre graphique
from tkinter import *
import tkinter as tk
import random as rd
racine = Tk()
racine.title("Jeu de couleurs")
racine.geometry("900x600")
racine.config(background="azure2")

#ajout d'un premier texte 
#label_text = Label(racine, text="Tapez la couleur des mots et pas le texte des mots !", bg="azure2", font=("Cassia", 20))

#ajout des fonctions
def incremente():
    "Incrémente le compteur à chaque seconde"
    global compteur
    compteur -=1
    compteur_lbl['text'] = str(compteur)
    racine.after(1000, incremente)

compteur = 30
compteur_lbl = tk.Label(racine, text=str(compteur), font=("", 16))
compteur_lbl.pack()

#Apparition du mot du milieu
couleurs = ['deep sky blue','firebrick1','spring green2','Gold','DeepPink2','chocolate1','white']
mots = ['Bleu','Rouge','Vert','Jaune','Rose','Orange','Blanc','Violet','Noir','Marron','Gris','Beige']
label_title = Label(racine, text=rd.choice(mots), font=("Cassia",20), fg=rd.choice(couleurs), bg='azure2')
label_title.pack()
    

label_text = Label(racine, text="Tapez la couleur des mots et pas le texte des mots !", bg="azure2", font=("Cassia", 20))









#ajout des boutons
first_button = Button(racine, text="Démarrer", command=incremente)
second_button = Button(racine, text="réinitialiser")
third_button = Button(racine, text='Bleu', bg='deep sky blue')
fourth_button = Button(racine, text='Rouge', bg='firebrick1')
fifth_button = Button(racine, text='Vert', bg='spring green2')
sixth_button = Button(racine, text='Jaune', bg='Gold')
seventh_button = Button(racine, text='Rose', bg='DeepPink2')
eighth_button = Button(racine, text='Orange', bg='chocolate1')
ninth_button = Button(racine, text='Blanc', bg='white')
#Affichage
label_title.pack()
label_text.pack()
first_button.pack(side =RIGHT, pady =50)
second_button.pack(side =LEFT, pady =50)
third_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
fourth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
fifth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
sixth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
seventh_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
eighth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
ninth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)

racine.after(1000,incremente)
racine.mainloop()
lilala
