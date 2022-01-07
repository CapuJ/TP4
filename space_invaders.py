#Header
"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

#Importation des modules nécessaires
from tkinter import Button, Label, Tk, Canvas, messagebox, PhotoImage
import os
from random import randint
from time import sleep
import structure_file as fl
# Initialisation

Largeur=480
Hauteur=320
tirs_alien = []
tirs_vaisseau = []
class alien:
    def __init__(self, x0, y0, x1, y1, rayon, sens, jeu):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.rayon = rayon
        self.sens = sens
        self.id_tk = jeu.create_oval(x0, y0, x1, y1, fill = 'green')
        self.deplacement(jeu, 2, 15)
    def deplacement(self, jeu, pas_x, pas_y):
        if (self.x0 + self.sens * pas_x) < 0 or (self.x1 + self.sens * pas_x) > Largeur:
            self.sens *= -1
            self.y0 = self.y0 + pas_y
            self.y1 = self.y1 + pas_y
        self.x0 = self.x0 + self.sens * pas_x
        self.x1 = self.x1 + self.sens * pas_x 
        jeu.coords(self.id_tk, self.x0, self.y0, self.x1, self.y1)
        jeu.after(20, self.deplacement, jeu, pas_x, pas_y)
    def tir(self, tirs_alien, jeu):
        tirs_alien += [tir_alien(self, 15, jeu)]
        delai = randint(2000, 5000)
        jeu.after(delai, self.tir, tirs_alien, jeu)
        
class tir_alien:
    def __init__(self, alien, longueur, jeu):
        self.x = alien.x0 + alien.rayon
        self.y0 = alien.y1
        self.y1 = alien.y1 + longueur
        self.id_tk = jeu.create_line(self.x, self.y0, self.x, self.y1, fill="yellow")
        self.deplacement(jeu)
    def deplacement(self, jeu):
        self.y0 += 10
        self.y1 += 10
        jeu.coords(self.id_tk, self.x, self.y0, self.x, self.y1)
        jeu.after(20, self.deplacement, jeu)

class vaisseau:
    def __init__(self,jeu):
        self.x0 = Largeur/2 -10
        self.y0 = Hauteur - 5
        self.x1 = Largeur/2 + 10
        self.y1 = Hauteur - 25
        self.id_tk = jeu.create_rectangle(self.x0, self.y0, self.x1, self.y1, width=5, outline='dark cyan', fill='cyan')
    def deplacement(self, sens, jeu):
        self.x0 += sens * 20
        self.x1 += sens * 20
        if self.x0 < 0:
            self.x1 = Largeur
            self.x0 = Largeur - 20
        elif self.x1 > Largeur:
            self.x0 = 0
            self.x1 = 20
        jeu.coords(self.id_tk, self.x0, self.y0, self.x1, self.y1)
    def tir(self, tirs_vaisseau, jeu):
        tirs_vaisseau += [tir_vaisseau(self, 20, jeu)]

class tir_vaisseau:
    def __init__(self, vaisseau, longueur, jeu):
        self.x = vaisseau.x0 + 10
        self.y0 = vaisseau.y0 - longueur
        self.y1 = vaisseau.y0
        self.id_tk = jeu.create_line(self.x, self.y0, self.x, self.y1, fill="red")
        self.deplacement(jeu)
    def deplacement(self, jeu):
        self.y0 -= 10
        self.y1 -= 10
        jeu.coords(self.id_tk, self.x, self.y0, self.x, self.y1)
        jeu.after(20, self.deplacement, jeu)


def Clavier(event):
    touche = event.keysym
    if touche =='Right':
        vaisseau1.deplacement(1, jeu)
    if touche =='Left':
        vaisseau1.deplacement(-1, jeu)
    if touche =='space':
        vaisseau1.tir(tirs_vaisseau, jeu)
        print(tirs_vaisseau[0].pos)
#Programme principal


fenetre = Tk()
fenetre.title("Space invaders")
chemin = os.path.join(os.path.dirname(__file__), "f1.gif") #permet de trouver a l'instant t l'emplacement du fichier python et de lui associer l'image 
photo=PhotoImage(file=chemin)
score = Label(fenetre, text='Score:')
score.grid(row=0, column=0, sticky='w')
vies = Label(fenetre, text='Vies:  /3')
vies.grid(row=0, column=1, sticky='w')
jeu = Canvas(fenetre, bg= 'dark blue' , width=Largeur, height=Hauteur)
item= jeu.create_image(0,0, image=photo)
jeu.grid(row=1, column= 0, rowspan=2)
bouton_recommencer = Button(fenetre, text="Nouveau Jeu", activebackground="cyan", background="green")
bouton_recommencer.grid(row=1, column=1)
bouton_quitter = Button(fenetre, text="Quitter le jeu", activebackground="cyan", background="red", command=fenetre.destroy)
bouton_quitter.grid(row=2, column=1)
vaisseau1 = vaisseau(jeu)
alien1 = alien(10, 10, 40, 40, 15, 1, jeu)
delai = randint(2000, 5000)
fenetre.after(delai, alien1.tir, tirs_alien, jeu)
jeu.focus_set()
jeu.bind('<Key>', Clavier)
fenetre.mainloop()

