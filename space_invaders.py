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

largeur=480
hauteur=320
tirs_alien = []
tirs_vaisseau = []

class alien:
    def __init__(self, x0, y0, x1, y1, rayon, jeu):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.rayon = rayon
        self.id_tk = jeu.create_oval(x0, y0, x1, y1, fill = 'green')
        #self.deplacement(jeu, 5, 15)
    def deplacement(self, jeu, pas_x, pas_y, debordement, sens):
        if debordement:
            self.y0 = self.y0 + pas_y
            self.y1 = self.y1 + pas_y
        else:
            self.x0 = self.x0 + pas_x * sens
            self.x1 = self.x1 + pas_x * sens
        jeu.coords(self.id_tk, self.x0, self.y0, self.x1, self.y1)
    def tir(self, tirs_alien, jeu):
        tirs_alien += [tir_alien(self, 15, jeu)]
        delai = randint(2000, 5000)
        jeu.after(delai, self.tir, tirs_alien, jeu)
    def collision(self, vaisseau):
        return vaisseau1.y1 < self.y1 < vaisseau.y0 and (vaisseau.x0 <self.x0 < vaisseau.x1) or (vaisseau.x0 < self.x1 < vaisseau.x1)

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
        self.x0 = largeur/2 -10
        self.y0 = hauteur - 5
        self.x1 = largeur/2 + 10
        self.y1 = hauteur - 25
        self.id_tk = jeu.create_rectangle(self.x0, self.y0, self.x1, self.y1, width=5, outline='dark cyan', fill='cyan')
    def deplacement(self, sens, jeu):
        self.x0 += sens * 20
        self.x1 += sens * 20
        if self.x0 < 0:
            self.x1 = largeur
            self.x0 = largeur - 20
        elif self.x1 > largeur:
            self.x0 = 0
            self.x1 = 20
        jeu.coords(self.id_tk, self.x0, self.y0, self.x1, self.y1)
    def tir(self, tirs_vaisseau, jeu):
        tirs_vaisseau += [tir_vaisseau(self, 20, jeu, tirs_vaisseau)]

class tir_vaisseau:
    def __init__(self, vaisseau, longueur, jeu, tirs_vaisseaux):
        self.x = vaisseau.x0 + 10
        self.y0 = vaisseau.y0 - longueur
        self.y1 = vaisseau.y0
        self.id_tk = jeu.create_line(self.x, self.y0, self.x, self.y1, fill="red")
        self.deplacement(jeu, tirs_vaisseau)
    def deplacement(self, jeu, tirs_vaisseau):
        self.y0 -= 10
        self.y1 -= 10
        jeu.coords(self.id_tk, self.x, self.y0, self.x, self.y1)
        if self.y0 < 0:
            jeu.delete(self.id_tk)
            tirs_vaisseau.remove(self)
        else: 
            jeu.after(20, self.deplacement, jeu, tirs_vaisseau)

class groupe_aliens:
    def __init__(self, jeu, nb_lignes, nb_colonnes, rayon_alien):
        self.aliens = []
        self.xmin = (largeur/2) - ((nb_lignes/2) * (2 *rayon_alien))
        self.xmax = (largeur/2) - ((nb_lignes/2) * (2 * rayon_alien)) + 2 * rayon_alien
        self.sens = 1
        x0 = self.xmin
        y0 = 10 - 2 * rayon_alien
        for j in range(nb_colonnes):
            x0 = self.xmin
            y0 += 2 * rayon_alien
            for i in range(nb_lignes):
                self.aliens += [alien(x0, y0, x0 + (2 * rayon_alien), y0 + (2 * rayon_alien), rayon_alien, jeu)]
                x0 += 2 * rayon_alien
        jeu.after(20, self.deplacement, 2, 15, jeu)
    def deplacement(self, pas_x, pas_y, jeu):
        print(self.sens)
        debordement_g = (self.xmin + self.sens * pas_x < 0)
        debordement_d = (self.xmax + self.sens * pas_x > largeur)
        print(self.xmin, self.xmax)
        if (debordement_g or debordement_d):
            self.sens *= -1
            for alien in self.aliens:
                alien.deplacement(jeu, pas_x, pas_y, True, self.sens)
                if alien.x0 < self.xmin:
                    self.xmin = alien.x0
                if alien.x1 > self.xmax:
                    self.xmax = alien.x1
        else:
            self.xmax = 0
            self.xmin = largeur
            for alien in self.aliens:
                alien.deplacement(jeu, pas_x, pas_y, False, self.sens)
                if alien.x0 < self.xmin:
                    self.xmin = alien.x0
                if alien.x1 > self.xmax:
                    self.xmax = alien.x1
        jeu.after(20, self.deplacement, pas_x, pas_y, jeu)
    
            



def Clavier(event):
    touche = event.keysym
    if touche =='Right':
        vaisseau1.deplacement(1, jeu)
    if touche =='Left':
        vaisseau1.deplacement(-1, jeu)
    if touche =='space':
        vaisseau1.tir(tirs_vaisseau, jeu)


#Programme principal

fenetre = Tk()
fenetre.title("Space invaders")
chemin = os.path.join(os.path.dirname(__file__), "f1.gif") #permet de trouver a l'instant t l'emplacement du fichier python et de lui associer l'image 
photo=PhotoImage(file=chemin)
score = Label(fenetre, text='Score:')
score.grid(row=0, column=0, sticky='w')
vies = Label(fenetre, text='Vies:  /3')
vies.grid(row=0, column=1, sticky='w')
jeu = Canvas(fenetre, bg= 'dark blue' , width=largeur, height=hauteur)
item= jeu.create_image(0,0, image=photo)
jeu.grid(row=1, column= 0, rowspan=2)
bouton_recommencer = Button(fenetre, text="Nouveau Jeu", activebackground="cyan", background="green")
bouton_recommencer.grid(row=1, column=1)
bouton_quitter = Button(fenetre, text="Quitter le jeu", activebackground="cyan", background="red", command=fenetre.destroy)
bouton_quitter.grid(row=2, column=1)
vaisseau1 = vaisseau(jeu)
delai = randint(2000, 5000)
groupe = groupe_aliens(jeu, 9, 4, 20)
#fenetre.after(delai, alien1.tir, tirs_alien, jeu)
jeu.focus_set()
jeu.bind('<Key>', Clavier)
fenetre.mainloop()

