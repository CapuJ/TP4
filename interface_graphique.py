#Header

"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

#Importation des modules nécessaires

from tkinter import Button, Label, Tk, Canvas

#Programme principal



fenetre = Tk()


score = Label(fenetre, text='Score:')
score.grid(row=0, column=0, sticky='w')
jeu = Canvas(fenetre, bg= 'black')
jeu.grid(row=1, column= 0, rowspan=2)
bouton_recommencer = Button(fenetre, text="New game")
bouton_recommencer.grid(row=1, column=1)
bouton_quitter = Button(fenetre, text="Quit", command=fenetre.destroy)
bouton_quitter.grid(row=2, column=1)
fenetre.mainloop()