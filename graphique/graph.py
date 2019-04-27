#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tkinter import *
from jeux.jeux import Jeux


class FGraphique:

    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title('Menu')
        self.bouton = Button(self.fenetre, text="Jeux", command=Jeux)
        self.bouton.pack()
        self.fenetre.mainloop()
