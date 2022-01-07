#Header
"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

#Importation des modules nécessaires
from tkinter import Button, Label, Tk, Canvas, messagebox
from random import randint
from time import sleep
# Initialisation

Largeur=480
Hauteur=320

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
        fenetre.after(delai, alien1.tir, tirs_alien, jeu)
        
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
        fenetre.after(20, self.deplacement, jeu)



#Programme principal

tirs_alien = []

fenetre = Tk()
fenetre.title("Space invaders")
score = Label(fenetre, text='Score:')
score.grid(row=0, column=0, sticky='w')
jeu = Canvas(fenetre, bg= 'dark blue', width=Largeur, height=Hauteur)
jeu.grid(row=1, column= 0, rowspan=2)
bouton_recommencer = Button(fenetre, text="New game", activebackground="cyan", background="green")
bouton_recommencer.grid(row=1, column=1)
bouton_quitter = Button(fenetre, text="Quit Game", activebackground="cyan", background="red", command=fenetre.destroy)
bouton_quitter.grid(row=2, column=1)

alien1 = alien(10, 10, 40, 40, 15, 1, jeu)
delai = randint(2000, 5000)
fenetre.after(delai, alien1.tir, tirs_alien, jeu)

fenetre.mainloop()

