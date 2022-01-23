#Header
"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

## Importation des modules nécessaires ##

from PIL import Image, ImageTk
from tkinter import Button, Label, Tk, Canvas, messagebox, PhotoImage, StringVar
import os
from random import randint



## Initialisation ##

largeur=960
hauteur=640
taille_vaisseau = 80
dimensions_vaisseau = (taille_vaisseau, int((250/532)*taille_vaisseau))
taille_alien = 50
dimensions_alien = (taille_alien, taille_alien)

class space_invaders:
    def __init__(self, jeu):
        self.tirs_alien = []
        self.tirs_vaisseau = []
        self.vaisseau1 = None
        self.groupe = None
        self.boss = None
        self.protections = None 
        self.jeu = jeu
    def init_game(self):
        self.vaisseau1 = vaisseau(self.jeu, dimensions_vaisseau, photo_vaisseau)
        self.protections = protection(jeu, 30, photo_bloc)
        self.groupe = groupe_aliens(self.jeu, 9, 4, (taille_alien/2), photo_alien)
        self.boss = super_alien(taille_alien/2, self.jeu, photo_super_alien)
        
    def game_over(self):
        self.vaisseau1 = None
        self.groupe = None
        self.boss = None
        self.tirs_alien = []
        self.tirs_vaisseau = []
        self.jeu.delete('all')
        self.jeu.create_image(0,0, image=photo, anchor = 'nw')
        messagebox.showinfo('Game Over', 'Vous avez perdu')
    def new_game(self):
        self.vaisseau1 = None
        self.groupe = None
        self.boss = None
        self.tirs_alien = []
        self.tirs_vaisseau = []
        self.jeu.delete('all')
        self.jeu.create_image(0,0, image=photo, anchor = 'nw')
        self.init_game()
        
class alien: 
#Cette classe met en place toute les doneés liées a l'alien
    def __init__(self, x0, y0, x1, y1, rayon, jeu, photo):
    #initialisation de l'alien
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.rayon = rayon
        self.id_tk = jeu.create_image(self.x0, self.y0, image=photo, anchor='nw')
    def deplacement(self, jeu, pas_x, pas_y, debordement, sens):
        if debordement:
            self.y0 = self.y0 + pas_y
            self.y1 = self.y1 + pas_y
        else:
            self.x0 = self.x0 + pas_x * sens
            self.x1 = self.x1 + pas_x * sens
        jeu.coords(self.id_tk, self.x0, self.y0)
    def tir(self, tirs_alien, jeu, protections):
        tirs_alien += [tir_alien(self, 15, jeu, partie.vaisseau1, vies, protections, tirs_alien)]
    def collision(self, vaisseau):
        return vaisseau.y1 < self.y1 < vaisseau.y0 and (vaisseau.x0 <self.x0 < vaisseau.x1) or (vaisseau.x0 < self.x1 < vaisseau.x1)


class tir_alien:
    def __init__(self, alien, longueur, jeu, cible, vies, protections, tirs_alien):
        self.x = alien.x0 + alien.rayon
        self.y0 = alien.y1
        self.y1 = alien.y1 + longueur
        self.id_tk = jeu.create_line(self.x, self.y0, self.x, self.y1, fill="yellow")
        self.deplacement(jeu, cible, vies, protections, tirs_alien)
    def deplacement(self, jeu, cible, vies, protections, tirs_alien):
        self.y0 += 10
        self.y1 += 10
        jeu.coords(self.id_tk, self.x, self.y0, self.x, self.y1)
        collision = self.collision(cible, vies, jeu, protections, tirs_alien)
        if self.y0 > hauteur:
            jeu.delete(self.id_tk)
            partie.tirs_alien.remove(self)
        elif not collision:
            jeu.after(20, self.deplacement, jeu, cible, vies, protections, tirs_alien)
    def collision(self, cible, vies, jeu, protections, tirs_alien):
        meme_ligne = cible.y0 < self.y1 < cible.y1
        meme_colonne = cible.x0 < self.x < cible.x1
        if meme_colonne and meme_ligne:
            jeu.delete(self.id_tk)
            tirs_alien.remove(self)
            vies.update()
            if vies.int_vie == 0:
                partie.game_over()
            return True
        for bloc in protections.liste_blocs:
            meme_ligne = bloc.y0 <= self.y0 <= bloc.y1
            meme_colonne = bloc.x0 <= self.x <= bloc.x1
            if meme_colonne and meme_ligne:
                jeu.delete(self.id_tk)
                tirs_alien.remove(self)
                jeu.delete(bloc.id_tk)
                protections.liste_blocs.remove(bloc)
                return True
        return False



class super_alien:
    def __init__(self, rayon, jeu, photo):
        self.x0 = largeur/2 - rayon
        self.y0 = -10 - 3 * rayon
        self.x1 = self.x0 + 2 * rayon
        self.y1 = self.y0 + 2 * rayon
        self.rayon = rayon
        self.id_tk = jeu.create_image(self.x0, self.y0, image=photo, anchor='nw')
        jeu.after(20000, self.descente, jeu, 2)
        jeu.after(22000, self.tir, partie.tirs_alien, jeu, partie.protections)
    def descente(self, jeu, pas):
        self.y0 += pas
        self.y1 += pas
        jeu.coords(self.id_tk, self.x0, self.y0)
        if self.y0 < 10:
            jeu.after(20, self.descente, jeu, pas)
        else:
            jeu.after(20, self.deplacement, jeu, pas, 1)
    def deplacement(self, jeu, pas, sens):
        debordement_d = (self.x0 + pas * sens < 0)
        debordement_g = (self.x1 + pas * sens > largeur)
        if debordement_d or debordement_g:
            sens *= -1
        self.x0 = self.x0 + pas * sens
        self.x1 = self.x1 + pas * sens
        jeu.coords(self.id_tk, self.x0, self.y0)
        jeu.after(10, self.deplacement, jeu, pas, sens)
    def tir(self, tirs_alien, jeu, protections):
        tirs_alien += [tir_alien(self, 15, jeu, partie.vaisseau1, vies, protections, tirs_alien)]
        delai = randint(500, 1500)
        jeu.after(delai, self.tir, tirs_alien, jeu, partie.protections)

class vaisseau:
    def __init__(self, jeu, dimensions, photo):
        largeur_vaisseau, hauteur_vaisseau = dimensions
        self.x0 = largeur/2 - (largeur_vaisseau/2)
        self.y0 = hauteur - 5 - hauteur_vaisseau
        self.x1 = largeur/2 + (largeur_vaisseau/2)
        self.y1 = hauteur - 5 
        self.charge = True
        self.id_tk = jeu.create_image(self.x0, self.y0, image=photo, anchor='nw')
    def deplacement(self, sens, jeu, dimensions):
        largeur_vaisseau, hauteur_vaisseau = dimensions
        self.x0 += sens * 10
        self.x1 += sens * 10
        if self.x0 < 0:
            self.x1 = largeur
            self.x0 = largeur - largeur_vaisseau
        elif self.x1 > largeur:
            self.x0 = 0
            self.x1 = largeur_vaisseau
        jeu.coords(self.id_tk, self.x0, self.y0)
    def tir(self, tirs_vaisseau, jeu, groupe, score, super_alien, protections):
        if self.charge:
            tirs_vaisseau += [tir_vaisseau(self, 20, jeu, tirs_vaisseau, groupe, score, super_alien, protections)]
            self.charge = False
            jeu.after(500, self.reload)
    def reload(self):
        self.charge = True

class tir_vaisseau:
    def __init__(self, vaisseau, longueur, jeu, tirs_vaisseau, groupe, score, super_alien, protections):
        self.x = vaisseau.x0 + taille_vaisseau/2   
        self.y0 = vaisseau.y0 - longueur
        self.y1 = vaisseau.y0
        self.id_tk = jeu.create_line(self.x, self.y0, self.x, self.y1, fill="red")
        self.deplacement(jeu, tirs_vaisseau, groupe, score, super_alien, protections)
    def deplacement(self, jeu, tirs_vaisseau, groupe, score, super_alien, protections):
        self.y0 -= 10
        self.y1 -= 10
        jeu.coords(self.id_tk, self.x, self.y0, self.x, self.y1)
        collision = self.collision(groupe, tirs_vaisseau, jeu, score, super_alien, protections)
        if self.y0 < 0:
            jeu.delete(self.id_tk)
            tirs_vaisseau.remove(self)
        elif not collision:
            jeu.after(20, self.deplacement, jeu, tirs_vaisseau, groupe, score, super_alien, protections)
    def collision(self, groupe, tirs_vaisseau, jeu, score, super_alien, protections):
        for alien in groupe.aliens:
            meme_ligne = alien.y0 <= self.y0 <= alien.y1
            meme_colonne = alien.x0 <= self.x <= alien.x1
            if meme_colonne and meme_ligne:
                jeu.delete(self.id_tk)
                tirs_vaisseau.remove(self)
                jeu.delete(alien.id_tk)
                groupe.aliens.remove(alien)
                score.update(10)
                return True
        meme_ligne = super_alien.y0 <= self.y0 <= super_alien.y1
        meme_colonne = super_alien.x0 <= self.x <= super_alien.x1
        if meme_colonne and meme_ligne:
            jeu.delete(self.id_tk)
            tirs_vaisseau.remove(self)
            jeu.delete(super_alien.id_tk)
            super_alien.y0 -= 100
            super_alien.y1 -= 100
            score.update(150)
            return True
        for bloc in protections.liste_blocs:
            meme_ligne = bloc.y0 <= self.y0 <= bloc.y1
            meme_colonne = bloc.x0 <= self.x <= bloc.x1
            if meme_colonne and meme_ligne:
                jeu.delete(self.id_tk)
                tirs_vaisseau.remove(self)
                jeu.delete(bloc.id_tk)
                protections.liste_blocs.remove(bloc)
                return True
        return False
        
class groupe_aliens:
    def __init__(self, jeu, nb_lignes, nb_colonnes, rayon_alien, photo):
        self.aliens = []
        self.xmin = (largeur/2) - ((nb_lignes/2) * (2 *rayon_alien)) - ((nb_lignes - 1) * 4)
        self.xmax = (largeur/2) - ((nb_lignes/2) * (2 * rayon_alien)) + 2 * rayon_alien 
        self.sens = 1
        x0 = self.xmin
        y0 = 10 - 2 * rayon_alien
        for _ in range(nb_colonnes):
            x0 = self.xmin
            y0 += 2 * rayon_alien + 4
            for _ in range(nb_lignes):
                self.aliens += [alien(x0, y0, x0 + (2 * rayon_alien), y0 + (2 * rayon_alien), rayon_alien, jeu, photo)]
                x0 += 2 * rayon_alien + 4
        jeu.after(20, self.deplacement, 2, 15, jeu)
        delai = randint(500, 1500)
        jeu.after(delai, self.tir, partie.tirs_alien, jeu, partie.protections)
    def deplacement(self, pas_x, pas_y, jeu):
        debordement_g = (self.xmin + self.sens * pas_x < 0)
        debordement_d = (self.xmax + self.sens * pas_x > largeur)
        if (debordement_g or debordement_d):
            self.sens *= -1
            self.xmax = 0
            self.xmin = largeur
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
    def tir(self, tirs_alien, jeu, protections):
        n = len(self.aliens)
        ind_tireur = randint(0, n - 1)
        tireur = self.aliens[ind_tireur]
        tireur.tir(tirs_alien, jeu, protections)
        delai = randint(500, 1500)
        jeu.after(delai, self.tir, tirs_alien, jeu, protections)

class bloc_protection:
    def __init__(self, x0, y0, largeur, photo, jeu):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0 + largeur
        self.y1 = y0 + largeur
        self.id_tk = jeu.create_image(self.x0, self.y0, image=photo, anchor='nw')

class protection:
    def __init__(self, jeu, largeur_bloc, photo_bloc):
        self.liste_blocs = []
        debut_x = 60
        debut_y = 440
        for _ in range(3):
            x0 = debut_x 
            y0 = debut_y
            for _ in range(3):
                x0 = debut_x
                for _ in range(8):
                    self.liste_blocs += [bloc_protection(x0, y0, largeur_bloc, photo_bloc, jeu)]
                    x0 += 30
                y0 += 30
            debut_x += 300

class vie:
    def __init__(self):
        self.int_vie = 3
        self.str_vie = StringVar()
        self.str_vie.set('Vie:  ' + str(self.int_vie) + '/3')
    def update(self):
        self.int_vie -= 1
        self.str_vie.set('Vie:  ' + str(self.int_vie) + '/3')
class score:
    def __init__(self):
        self.int_score = 0
        self.str_score = StringVar()
        self.str_score.set('Score:  ' + str(self.int_score))
    def update(self, points):
        self.int_score += points
        self.str_score.set('Score:  ' + str(self.int_score))



def Clavier(event):
    touche = event.keysym
    if touche =='Right':
        partie.vaisseau1.deplacement(1, jeu, dimensions_vaisseau)
    if touche =='Left':
        partie.vaisseau1.deplacement(-1, jeu, dimensions_vaisseau)
    if touche =='space':
        partie.vaisseau1.tir(partie.tirs_vaisseau, jeu, partie.groupe, score1, partie.boss, partie.protections)
        


def charge_image(chemin, dimensions):
    image = Image.open(chemin)
    return image.resize(dimensions, Image.ANTIALIAS)


## Programme principal ##

#création de la fenêtre
fenetre = Tk()
fenetre.title("Space invaders")




#recherche de la photo de fond
chemin = os.path.join(os.path.dirname(__file__), "f2.gif") #permet de trouver a l'instant t l'emplacement du fichier python et de lui associer l'image 
photo=PhotoImage(file=chemin)

#affichage du score
score1 = score()
score_label = Label(fenetre, textvariable=score1.str_score)
score_label.grid(row=0, column=0, sticky='w')

#affichage du nombre de vies
vies = vie()
vies_label = Label(fenetre, textvariable=vies.str_vie)
vies_label.grid(row=0, column=1, sticky='w')

#affichage du canvas
jeu = Canvas(fenetre, bg= 'dark blue', width=largeur, height=hauteur)
jeu.grid(row=1, column= 0, rowspan=2)

#création de l'image de fond sur le canvas
item = jeu.create_image(0,0, image=photo, anchor = 'nw')

#création de l'image des aliens
chemin_alien = os.path.join(os.path.dirname(__file__), "alien.png")
photo_alien = ImageTk.PhotoImage(charge_image(chemin_alien, dimensions_alien))

#création de l'image du vaisseau
chemin_vaisseau = os.path.join(os.path.dirname(__file__), "vaisseau.png")
photo_vaisseau = ImageTk.PhotoImage(charge_image(chemin_vaisseau, dimensions_vaisseau))

#Création de l'image du boss 
chemin_super_alien = os.path.join(os.path.dirname(__file__), "super_alien.png")
photo_super_alien = ImageTk.PhotoImage(charge_image(chemin_super_alien, dimensions_alien))

#création de l'image des blocs: 
chemin_bloc = os.path.join(os.path.dirname(__file__), "bloc.gif")
photo_bloc = ImageTk.PhotoImage(charge_image(chemin_bloc, (30,30)))


#Initialisation jeu

partie = space_invaders(jeu)
partie.init_game()

#création du boutton "Nouveau Jeu"
bouton_recommencer = Button(fenetre, text="Nouveau Jeu", activebackground="cyan", background="green", command=partie.new_game) 
bouton_recommencer.grid(row=1, column=1)

#création du boutton "Quitter le Jeu"
bouton_quitter = Button(fenetre, text="Quitter le jeu", activebackground="cyan", background="red", command=fenetre.destroy)
bouton_quitter.grid(row=2, column=1)

jeu.focus_set()
jeu.bind('<Key>', Clavier)
fenetre.mainloop()
 