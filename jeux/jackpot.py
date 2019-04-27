#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
from random import randint
from errors import *


class JackPot:
    capital = 1000
    mise = None
    resultat = [0]*3
    signes = [None]*3

    def __init__(self):
        print('\nJeu JackPot\nCapital initial :', self.capital, '.')
        while True:
            try:
                mise = int(input('\nEntrer une mise : '))
                if self.verifierMise(mise):
                    self.mise = mise
                    self.capital -= mise
                    self.demarrerCylindre()
                    self.calculerGain()
                    self.afficherCylindre()
                    self.afficherGain()
                    if self.capital == 0:
                        print('Vous n\'avez plus de capital !')
                        break
                    elif input('Voulez-vous continuer ? (Y/N) ') == 'N':
                        print('Vous repartez avec', self.capital)
                        break
                else:
                    BadVerification()
            except:
                NoInt()

    def verifierMise(self, mise):
        if mise <= self.capital:
            return True
        else:
            return False

    def demarrerCylindre(self):
        for i in range(3):
            self.resultat[i] = randint(0, len(string.printable)-1)
            # print(self.resultat[i])
            self.signes[i] = string.printable[self.resultat[i]]
            # print(string.printable[self.resultat[i]])
        pass

    def calculerGain(self):
        # 3 signes identiques
        if self.signes[0] == self.signes[1] and self.signes[1] == self.signes[2]:
            self.mise *= 100
        # 3 signes qui se suivent
        elif self.resultat[0] + 1 == self.resultat[1] and self.resultat[1] + 1 == self.resultat[2]:
            self.mise *= 50
        # 3 chiffres
        elif self.signes[0] in string.digits and self.signes[1] in string.digits and self.signes[2] in string.digits:
            self.mise *= 30
        # 3 majuscules
        elif self.signes[0] in string.ascii_uppercase and self.signes[1] in string.ascii_uppercase and self.signes[2] in string.ascii_uppercase:
            self.mise *= 30
        # 3 minuscules
        elif self.signes[0] in string.ascii_lowercase and self.signes[1] in string.ascii_lowercase and self.signes[2] in string.ascii_lowercase:
            self.mise *= 25
        # 2 signes identiques
        elif self.signes[0] == self.signes[1] or self.signes[0] == self.signes[2] or self.signes[1] == self.signes[2]:
            self.mise *= 15
        # 3 signes croissants
        elif self.resultat[0] < self.resultat[1] < self.resultat[2]:
            self.mise *= 5
        # 3 signes décroissants
        elif self.resultat[0] > self.resultat[1] > self.resultat[2]:
            self.mise *= 2
        else:
            self.mise = 0
        self.capital += self.mise

    def afficherCylindre(self):
        print('Mise :', self.mise, '\n', self.signes[0], ' ', self.signes[1], ' ', self.signes[2])
        pass

    def afficherGain(self):
        print('Votre capital est de', self.capital, '.')
        pass
