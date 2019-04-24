#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from errors import *


class CerclesColores:
    taille = None
    couleur = None
    couleurs = ['black', 'blue', 'green', 'red']
    x1 = 10
    y1 = 190
    x2 = 190
    y2 = 10

    def __init__(self):
        print('\nJeu Télécran')
        try:
            taille = int(input('Entrer la taille : '))
            couleur = input('Entrer la couleur : ')
            if self.verifierTaille(taille) and self.verifierCouleur(couleur):
                self.taille = taille
                self.couleur = couleur
                self.creationFenetre()
            else:
                BadVerification()
        except:
            NoInt()

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

    def creationFenetre(self):
        self.fen1 = Tk()
        self.fen1.title('Cercles Colorés')
        self.can = Canvas(self.fen1, bg='dark grey', height=200, width=200)
        self.can.pack(side=LEFT)
        self.bou2 = Button(self.fen1, text='Tracer une ligne', command=self.dessiner())
        self.bou2.pack()
        self.fen1.mainloop()

    def dessiner(self):
        for i in range(20):
            self.can.create_line(self.x1, self.y1, self.x2, self.y2, width=2, fill=self.couleur)

            self.y2 += 10
            self.y1 -= 10


