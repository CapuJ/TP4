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
pas = 1

PosX=230
PosY=300
Largeur=480
Hauteur=320


#Programme principal

def deplacement_alien():
    global x0_alien, y0_alien, x1_alien, y1_alien, rayon, sens
    if (x0_alien + sens * pas) < 0 or (x1_alien + sens * pas) > Largeur:
        sens *= -1
    x0_alien = x0_alien + sens * pas
    x1_alien = x1_alien + sens * pas 
    jeu.coords(alien, x0_alien, y0_alien, x1_alien, y1_alien)
    fenetre.after(20, deplacement_alien)

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







Vaisseau=jeu.create_rectangle(PosX-10,PosY-10, PosX+10, PosY+10,width=5, outline='blue', fill='blue')

def Clavier(event):
    global PosX, PosY
    touche = event.keysym
    print(touche)
    if touche =='Right':
        PosX += 20
    if touche =='Left':
        PosX -= 20
    jeu.coords(Vaisseau, PosX -10, PosY -10, PosX+10, PosY +10,)


jeu.focus_set()
jeu.bind('<Key>', Clavier)




fenetre.mainloop() 

