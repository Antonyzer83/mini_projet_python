#!/usr/bin/env python
# -*- coding: utf-8 -*-

from errors import *


class Telecran:
    taille = None
    couleur = None
    couleurs = ['rouge', 'vert', 'bleu', 'orange', 'violet', 'rose', 'blanc', 'noir']

    def __init__(self):
        print('\nJeu Télécran')
        try:
            taille = int(input('\nEntrer la taille : '))
            couleur = input('Entrer la couleur : ')
            if self.verifierTaille(taille) and self.verifierCouleur(couleur):
                self.taille = taille
                self.couleur = couleur
            else:
                BadVerification()
        except:
            NoInt()

    def verifierTaille(self, taille):
        if taille < 10:
            return True
        else:
            return False

    def verifierCouleur(self, couleur):
        if couleur in self.couleurs:
            return True
        else:
            return False
