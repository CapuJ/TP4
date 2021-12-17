#Header
"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

#Importation des modules nécessaires
from tkinter import Button, Label, Tk, Canvas, messagebox

# Initialisation

tir_alien = None
x0_alien = 0
y0_alien = 10
x1_alien = 30
y1_alien = 40
rayon  = 15
sens = 1
pas_x = 2
pas_y = 15
tirs_alien  =[]

Largeur=480
Hauteur=320

# Fonctions
PosX=Largeur/2
PosY=Hauteur-15

xtir=PosX-10
ytir=PosY+10

#Programme principal

def deplacement_alien():
    global x0_alien, y0_alien, x1_alien, y1_alien, rayon, sens, PosX, PosY
    if (x0_alien + sens * pas_x) < 0 or (x1_alien + sens * pas_x) > Largeur:
        sens *= -1
        y0_alien = y0_alien + pas_y
        y1_alien = y1_alien + pas_y
    x0_alien = x0_alien + sens * pas_x
    x1_alien = x1_alien + sens * pas_x 
    jeu.coords(alien, x0_alien, y0_alien, x1_alien, y1_alien)
    if (PosY - 10 < y1_alien < PosY + 10) and ((PosX - 10 < x0_alien< PosX + 10 ) or (PosX - 10 < x1_alien < PosX + 10)):
        jeu.delete(vaisseau)
        messagebox.showinfo('', 'Vous avez perdu !')
    else:
        fenetre.after(20, deplacement_alien)

def creer_tir_alien():
    global x0_alien, y0_alien, x1_alien, y1_alien, rayon, tir_alien
    longueur_tir_alien = 20
    x_tir = x0_alien + rayon
    y0_tir = y1_alien
    y1_tir = y1_alien + longueur_tir_alien
    tir_alien = jeu.create_line(x_tir, y0_tir, x_tir, y1_tir, fill='yellow')
    deplacement_tir_alien()
    
def deplacement_tir_alien():
    global x0_alien, y0_alien, x1_alien, y1_alien, rayon, tir_alien
    x0_tir, y0_tir, x1_tir, y1_tir = jeu.coords(tir_alien)
    y0_tir += 10
    y1_tir += 10
    jeu.coords(tir_alien, x0_tir, y0_tir, x1_tir, y1_tir)



    
    

#Programme principal


def deplacement_tir():
    global ytir, rayon, sens, pas
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
jeu = Canvas(fenetre, bg= 'dark blue', width=Largeur, height=Hauteur)
jeu.grid(row=1, column= 0, rowspan=2)
bouton_recommencer = Button(fenetre, text="New game", activebackground="cyan", background="green")
bouton_recommencer.grid(row=1, column=1)
bouton_quitter = Button(fenetre, text="Quit Game", activebackground="cyan", background="red", command=fenetre.destroy)
bouton_quitter.grid(row=2, column=1)

alien = jeu.create_oval(x0_alien, y0_alien, x1_alien, y1_alien, fill="green")
deplacement_alien()

fenetre.after(1000, creer_tir_alien)

vaisseau=jeu.create_rectangle(PosX-10,PosY-10, PosX+10, PosY+10,width=5, outline='dark cyan', fill='cyan')


jeu.focus_set()
jeu.bind('<Key>', Clavier)


#tir=jeu.create_line(PosX, PosY-10, xtir+10, ytir+10, fill="yellow")


tir=jeu.create_line(PosX, PosY-10, xtir+10, ytir+10, fill="yellow")


fenetre.mainloop() 

