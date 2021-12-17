def Clavier(event):
    global PosX, PosY
    touche = event.keysym
    print(touche)
    if touche =='>':
        PosX += 20
    if touche =='<':
        PosX -= 20
    jeu.coords(Vaisseau, PosX -10, PosY -10, PosX+10, PosY +10,)

PosX=100
PosY=0

Vaisseau=jeu.create_rectangle(PosX-10,PosY-10, PosX+10, PosY+10,width=5, outline='blue', fill='blue')
jeu.focus_set()
jeu.blind('<Key>', Clavier)
