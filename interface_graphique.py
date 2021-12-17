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
fenetre.title("Space invaders")
jeu = Canvas(fenetre, bg= 'black')
jeu.pack(side='left')
bouton_recommencer = Button(fenetre, text="New game")
bouton_recommencer.pack(side='bottom', padx=5)
bouton_quitter = Button(fenetre, text="Quit", command=fenetre.destroy)
bouton_quitter.pack(side='top', padx=5, pady=10)
fenetre.mainloop()