#Header
"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

#Importation des modules nécessaires
from tkinter import Button, Label, Tk, Canvas

# Initialisation

x0_alien = 0
y0_alien = 10
x1_alien = 30
y1_alien = 40
rayon  = 15
sens = 1
pas = 10

Largeur=480
Hauteur=320

PosX=Largeur/2
PosY=Hauteur-15

xtir=PosX-10
ytir=PosY+10

#Programme principal

def deplacement_alien():
    global x0_alien, y0_alien, x1_alien, y1_alien, rayon, sens
    if (x0_alien + sens * pas) < 0 or (x1_alien + sens * pas) > Largeur:
        sens *= -1
    x0_alien = x0_alien + sens * pas
    x1_alien = x1_alien + sens * pas 
    jeu.coords(alien, x0_alien, y0_alien, x1_alien, y1_alien)
    fenetre.after(20, deplacement_alien)


def deplacement_tir():
    global ytir, rayon, sens, pas
    tir=jeu.create_line(PosX, PosY-10, xtir+10, ytir+10, fill="yellow")
    ytir -= 10
    jeu.coords(tir, PosX, ytir-10, xtir+10, ytir+10)
    fenetre.after(20, deplacement_tir)



def Clavier(event):
    global PosX, PosY, xtir #,ytir
    touche = event.keysym
    if touche =='Right':
        PosX += 20
        xtir +=20
        if PosX>Largeur:
            PosX=0
            xtir=PosX-10
    if touche =='Left':
        PosX -= 20 
        xtir -= 20
        if PosX<0:
            PosX=Largeur
            xtir=Largeur-10
    if touche =='space':
        deplacement_tir()
        #if ytir<200:
           # jeu.delete(tir)
        
    jeu.coords(vaisseau, PosX -10, PosY -10, PosX+10, PosY +10,)
    



fenetre = Tk()
fenetre.title("Space invaders")
score = Label(fenetre, text='Score:')
score.grid(row=0, column=0, sticky='w')
jeu = Canvas(fenetre, bg= 'black', width=Largeur, height=Hauteur)
jeu.grid(row=1, column= 0, rowspan=2)
bouton_recommencer = Button(fenetre, text="New game")
bouton_recommencer.grid(row=1, column=1)
bouton_quitter = Button(fenetre, text="Quit", command=fenetre.destroy)
bouton_quitter.grid(row=2, column=1)

alien = jeu.create_oval(x0_alien, y0_alien, x1_alien, y1_alien, fill='white')
deplacement_alien()

vaisseau=jeu.create_rectangle(PosX-10,PosY-10, PosX+10, PosY+10,width=5, outline='blue', fill='blue')
jeu.focus_set()
jeu.bind('<Key>', Clavier)


#tir=jeu.create_line(PosX, PosY-10, xtir+10, ytir+10, fill="yellow")




fenetre.mainloop() 

