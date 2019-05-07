#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from errors import *


class CerclesColores:
    taille = None
    couleur = None
    couleurs = ['black', 'blue', 'green', 'red']
    x1 = 100
    y1 = 5
    x2 = 100
    y2 = 195

    def __init__(self):
        print('\nJeu Télécran')
        try:
            taille = int(input('Entrer la taille : '))
        except TypeError:
            NoInt()
        couleur = input('Entrer la couleur : ')
        if self.verifierTaille(taille) and self.verifierCouleur(couleur):
            self.taille = taille
            self.couleur = couleur
            self.fen1 = Tk()
            self.fen1.title('Cercles Colorés')
            self.can = Canvas(self.fen1, bg='dark grey', height=200, width=200)
            self.can.pack()
            self.bou2 = Button(self.fen1, text='Tracer une ligne', command=self.dessiner())
            self.bou2.pack()
            self.fen1.mainloop()
        else:
            BadVerification()

    def verifierTaille(self, taille):
        if 1 <= taille <= 9:
            return True
        else:
            return False

    def verifierCouleur(self, couleur):
        if couleur in self.couleurs:
            return True
        else:
            return False

    def dessiner(self):
        while self.x1 <= 195 and self.x2 >= 5:
            self.can.create_line(self.x1, self.y1, self.x2, self.y2, width=2, fill=self.couleur)
            self.x1 += 5
            self.y1 += 5
            self.x2 -= 5
            self.y2 -= 5

        while self.x1 >= 100 and self.x2 <= 100:
            self.can.create_line(self.x1, self.y1, self.x2, self.y2, width=2, fill=self.couleur)
            self.x1 -= 5
            self.y1 += 5
            self.x2 += 5
            self.y2 -= 5
        pass
