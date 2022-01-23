#Header
"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

## Importation des modules nécessaires ##



from tkinter import Button, Label, Tk, Canvas, messagebox, PhotoImage, StringVar
import os
from random import randint
from PIL import Image, ImageTk


## Initialisation ##

largeur=960
hauteur=640
tirs_alien = []
tirs_vaisseau = []
score = 0



class alien: 
#Cette classe met en place toute les doneés liées a l'alien
    def __init__(self, x0, y0, x1, y1, rayon, jeu):
    #initialisation de l'alien
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.rayon = rayon
        self.id_tk = jeu.create_oval(x0, y0, x1, y1, fill = 'green')

    def deplacement(self, jeu, pas_x, pas_y, debordement, sens):
        if debordement:
            self.y0 = self.y0 + pas_y
            self.y1 = self.y1 + pas_y
        else:
            self.x0 = self.x0 + pas_x * sens
            self.x1 = self.x1 + pas_x * sens
        jeu.coords(self.id_tk, self.x0, self.y0, self.x1, self.y1)
    
    def tir(self, tirs_alien, jeu):
        tirs_alien += [tir_alien(self, 15, jeu, vaisseau1, vies)]
    def collision(self, vaisseau):
        return vaisseau.y1 < self.y1 < vaisseau.y0 and (vaisseau.x0 <self.x0 < vaisseau.x1) or (vaisseau.x0 < self.x1 < vaisseau.x1)




class tir_alien:
    def __init__(self, alien, longueur, jeu, cible, vies):
        self.x = alien.x0 + alien.rayon
        self.y0 = alien.y1
        self.y1 = alien.y1 + longueur
        self.id_tk = jeu.create_line(self.x, self.y0, self.x, self.y1, fill="yellow")
        self.deplacement(jeu, cible, vies)
    def deplacement(self, jeu, cible, vies):
        self.y0 += 10
        self.y1 += 10
        jeu.coords(self.id_tk, self.x, self.y0, self.x, self.y1)
        collision = self.collision(cible, vies, jeu)
        if self.y0 > hauteur:
            jeu.delete(self.id_tk)
            tirs_alien.remove(self)
        elif not collision:
            jeu.after(20, self.deplacement, jeu, cible, vies)
    def collision(self, cible, vies, jeu):
        meme_ligne = cible.y1 < self.y1 < cible.y0
        meme_colonne = cible.x0 < self.x < cible.x1
        if meme_colonne and meme_ligne:
            jeu.delete(self.id_tk)
            tirs_alien.remove(self)
            vies.update()
            if vies.int_vie == 0:
                messagebox.showinfo('Game over', 'Vous avez perdu')
            return True
        return False




class vaisseau:

    def __init__(self,jeu):
        self.x0 = largeur/2 - 20
        self.y0 = hauteur - 5
        self.x1 = largeur/2 + 20
        self.y1 = hauteur - 45
        self.charge = True
        self.id_tk = jeu.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill='cyan')
    def deplacement(self, sens, jeu):
        self.x0 += sens * 10
        self.x1 += sens * 10
        if self.x0 < 0:
            self.x1 = largeur
            self.x0 = largeur - 20
        elif self.x1 > largeur:
            self.x0 = 0
            self.x1 = 20
        jeu.coords(self.id_tk, self.x0, self.y0, self.x1, self.y1)
    def tir(self, tirs_vaisseau, jeu, groupe, score):
        if self.charge:
            tirs_vaisseau += [tir_vaisseau(self, 20, jeu, tirs_vaisseau, groupe, score)]
            self.charge = False
            jeu.after(500, self.reload)
    def reload(self):
        self.charge = True




class tir_vaisseau:
    def __init__(self, vaisseau, longueur, jeu, tirs_vaisseau, groupe, score):
        self.x = vaisseau.x0 + 10
        self.y0 = vaisseau.y0 - longueur
        self.y1 = vaisseau.y0
        self.id_tk = jeu.create_line(self.x, self.y0, self.x, self.y1, fill="red")
        self.deplacement(jeu, tirs_vaisseau, groupe, score)
    def deplacement(self, jeu, tirs_vaisseau, groupe, score):
        self.y0 -= 10
        self.y1 -= 10
        jeu.coords(self.id_tk, self.x, self.y0, self.x, self.y1)
        collision = self.collision(groupe, tirs_vaisseau, jeu, score)
        if self.y0 < 0:
            jeu.delete(self.id_tk)
            tirs_vaisseau.remove(self)
        elif not collision:
            jeu.after(20, self.deplacement, jeu, tirs_vaisseau, groupe, score)
    def collision(self, groupe, tirs_vaisseau, jeu, score):
        for alien in groupe.aliens:
            meme_ligne = alien.y0 < self.y0 < alien.y1
            meme_colonne = alien.x0 < self.x < alien.x1
            if meme_colonne and meme_ligne:
                jeu.delete(self.id_tk)
                tirs_vaisseau.remove(self)
                jeu.delete(alien.id_tk)
                groupe.aliens.remove(alien)
                #if groupe.aliens == []:
                 #   messagebox.showinfo('WINNER', 'Vous avez gagnez')
                  #  return True
                score.update()
                return True
        return False
        
    
        



class groupe_aliens:

    def __init__(self, jeu, nb_lignes, nb_colonnes, rayon_alien):
        self.aliens = []
        self.xmin = (largeur/2) - ((nb_lignes/2) * (2 *rayon_alien)) - ((nb_lignes - 1) * 4)
        self.xmax = (largeur/2) - ((nb_lignes/2) * (2 * rayon_alien)) + 2 * rayon_alien 
        self.sens = 1
        x0 = self.xmin
        y0 = 10 - 2 * rayon_alien
        for j in range(nb_colonnes):
            x0 = self.xmin
            y0 += 2 * rayon_alien + 4
            for i in range(nb_lignes):
                self.aliens += [alien(x0, y0, x0 + (2 * rayon_alien), y0 + (2 * rayon_alien), rayon_alien, jeu)]
                x0 += 2 * rayon_alien + 4
        jeu.after(20, self.deplacement, 2, 15, jeu)
        delai = randint(2000, 5000)
        jeu.after(delai, self.tir, tirs_alien, jeu)

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

    def tir(self, tirs_alien, jeu):
        n = len(self.aliens)
        ind_tireur = randint(0, n - 1)
        tireur = self.aliens[ind_tireur]
        tireur.tir(tirs_alien, jeu)
        delai = randint(500, 1500)
        jeu.after(delai, self.tir, tirs_alien, jeu)

 


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
    def update(self):
        self.int_score += 10
        self.str_score.set('Score:  ' + str(self.int_score))




def deplacer(event):
    touche = event.keysym
    if touche =='Right':
        vaisseau1.deplacement(1, jeu)
    if touche =='Left':
        vaisseau1.deplacement(-1, jeu)

def tirer(event):
    touche = event.keysym
    if touche =='space':
        vaisseau1.tir(tirs_vaisseau, jeu, groupe, score1)




class protection:

    def __init__(self):
        self.Blocs=[]
        self.XBloc=45
        self.YBloc=500
    
    def crea_Bloc(self, jeu, photo):
#cretion d'un bloc
        self.Bloc=jeu.create_image(self.XBloc,self.YBloc,anchor='nw', image=photo)
        return self.Bloc

    def crea_Ilots(self, jeu, photo):
        for i in range (0,54):  #nombre de repetition des blocs
            self.Blocs.append(self.crea_Bloc(jeu,  photo))
            if self.XBloc==195 or self.XBloc==510:
               self.XBloc+=135
            if self.XBloc==825:
                self.XBloc=45
                self.YBloc+=30
            else :
                self.XBloc+=30
        
    def colision(self, jeu):
        self.coords_bloc = self.jeu.coords(self.Bloc)
        self.elements = self.jeu.find_overlapping(*self.coords_bloc)
        if len(self.elements) > 1:
            for self.element in self.elements:
                self.jeu.remove(self.element)




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

#couleur de fond 
jeu = Canvas(fenetre, bg= 'dark blue', width=largeur, height=hauteur)

#création de l'image de fond sur le canvas
item= jeu.create_image(0,0, image=photo, anchor = 'nw')

#création de la grille
jeu.grid(row=1, column= 0, rowspan=2)

#création du boutton "Nouveau Jeu"
bouton_recommencer = Button(fenetre, text="Nouveau Jeu", activebackground="cyan", background="green") 
bouton_recommencer.grid(row=1, column=1)

#création du boutton "Quitter le Jeu"
bouton_quitter = Button(fenetre, text="Quitter le jeu", activebackground="cyan", background="red", command=fenetre.destroy)
bouton_quitter.grid(row=2, column=1)

vaisseau1 = vaisseau(jeu)
delai = randint(2000, 5000)
groupe = groupe_aliens(jeu, 9, 4, 25)



#création des blocs sur le canvas
chemin_bloc = os.path.join(os.path.dirname(__file__), "bloc.gif")
image_bloc = Image.open(chemin_bloc)
photo_bloc = ImageTk.PhotoImage(image_bloc)
variable=protection()
variable.crea_Ilots(jeu, photo_bloc)



#fenetre.after(delai, alien1.tir, tirs_alien, jeu)
jeu.focus_set()
jeu.bind('<Key>', deplacer)
jeu.bind("<KeyRelease>", tirer)
fenetre.mainloop()
