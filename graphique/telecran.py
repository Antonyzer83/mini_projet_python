#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *


class Telecran:
    x1 = 250
    y1 = 250
    x2 = 250
    y2 = 250

    def __init__(self):
        print('\nJeu Télécran')
        self.fen = Tk()
        self.fen.title('Télécran')
        self.can = Canvas(self.fen, bg='cyan', height=500, width=500)
        self.can.pack(side=LEFT)
        self.but_left = Button(self.fen, text='Gauche', command=self.deplacerGauche)
        self.but_left.pack(ipadx=10, ipady=5, padx=10, pady=10)
        self.but_right = Button(self.fen, text='Right', command=self.deplacerDroite)
        self.but_right.pack(ipadx=10, ipady=5, padx=10, pady=10)
        self.but_top = Button(self.fen, text='Haut', command=self.deplacerHaut)
        self.but_top.pack(ipadx=10, ipady=5, padx=10, pady=10)
        self.but_bottom = Button(self.fen, text='Bas', command=self.deplacerBas)
        self.but_bottom.pack(ipadx=10, ipady=5, padx=10, pady=10)
        self.but_delete = Button(self.fen, text='Reset', command=self.viderCanvas)
        self.but_delete.pack(ipadx=10, ipady=5, padx=10, pady=10)
        self.fen.mainloop()

    def deplacerGauche(self):
        self.x1 = self.x2
        self.y1 = self.y2
        self.x2 -= 10
        self.dessinerLigne()
        pass

    def deplacerDroite(self):
        self.x1 = self.x2
        self.y1 = self.y2
        self.x2 += 10
        self.dessinerLigne()
        pass

    def deplacerHaut(self):
        self.x1 = self.x2
        self.y1 = self.y2
        self.y2 -= 10
        self.dessinerLigne()
        pass

    def deplacerBas(self):
        self.x1 = self.x2
        self.y1 = self.y2
        self.y2 += 10
        self.dessinerLigne()
        pass

    def dessinerLigne(self):
        self.can.create_line(self.x1, self.y1, self.x2, self.y2, width=2)
        pass

    def viderCanvas(self):
        self.can.delete("all")
        self.x1 = 250
        self.y1 = 250
        self.x2 = 250
        self.y2 = 250
        pass
