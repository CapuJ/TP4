#Header

"""
Capucine Jumelle, Thomas Gabriel
17/12/2021
Interface du jeu Space Invaders
"""

#Importation des modules nécessaires

from tkinter import Button, Tk, Canvas

#Programme principal

x0_alien = 0
y0_alien = 10
x1_alien = 30
y1_alien = 40
rayon  = 15







fenetre = Tk()
fenetre.title("Space invaders")
score = Label(fenetre, text='Score:')
score.grid(row=0, column=0, sticky='w')
jeu = Canvas(fenetre, bg= 'black')
jeu.pack(side='left')
bouton_recommencer = Button(fenetre, text="New game")
bouton_recommencer.grid(row=1, column=1)
bouton_quitter = Button(fenetre, text="Quit", command=fenetre.destroy)
bouton_quitter.pack(side='top', padx=5, pady=10)
fenetre.mainloop()


<<<<<<< HEAD
=======
alien = jeu.create_oval(x0_alien, y0_alien, x1_alien, y1_alien, fill='white')

fenetre.mainloop()
>>>>>>> f4d00cd8ff4797ae7db52f4dc98d68a3395a8ddc
