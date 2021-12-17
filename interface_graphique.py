#Header

"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

#Importation des modules nécessaires

from tkinter import Button, Tk, Canvas

#Programme principal



fenetre = Tk()
jeu = Canvas(fenetre, bg= 'black')
jeu.pack()
bouton_recommencer = Button(fenetre, text="New game")
bouton_recommencer.pack()
bouton_quitter = Button(fenetre, text="Quit", command=fenetre.destroy)
bouton_quitter.pack()
fenetre.mainloop()