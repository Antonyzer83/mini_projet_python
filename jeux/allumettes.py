#!/usr/bin/env python
# -*- coding: utf-8 -*-


from errors import *
from random import randint


class Allumettes:
    nbre_allumettes = None
    nbre_max = None
    perdant = None

    def __init__(self):
        print('\nJeu Allumettes')
        try:
            nbre_allumettes = int(input('Entrer le nombre d\'allumettes total : '))
            nbre_max = int(input('Entrer le nombre max d\'allumettes à prendre : '))
            if self.verifierNbreMax(nbre_allumettes, nbre_max):
                self.nbre_allumettes = nbre_allumettes
                self.nbre_max = nbre_max
                choice = input('Taper O pour commencer : ')
                while self.nbre_allumettes > 1:
                    if choice == 'O':
                        try:
                            nbre_allumettes = int(input('J\'en prends : '))
                            if self.verifierPrendreAllumettes(nbre_allumettes):
                                if self.verifierDerniereAllumette():
                                    break
                                print(self.nbre_allumettes)
                                self.tourOrdinateur()
                                if self.verifierDerniereAllumette():
                                    break
                                print(self.nbre_allumettes)
                            else:
                                BadVerification()
                        except:
                            NoInt()
                    else:
                        self.tourOrdinateur()
                        if self.verifierDerniereAllumette():
                            break
                        print(self.nbre_allumettes)
                        try:
                            nbre_allumettes = int(input('J\'en prends : '))
                            self.verifierPrendreAllumettes(nbre_allumettes)
                            if self.verifierDerniereAllumette():
                                break
                            print(self.nbre_allumettes)
                        except:
                            NoInt()
                print('Plus d\'allumettes\nPerdant :', self.perdant)
            else:
                BadVerification()
        except:
            NoInt()

    def verifierNbreMax(self, nbre_allumettes, nbre_max):
        if nbre_allumettes > nbre_max:
            return True
        else:
            return False

    def verifierPrendreAllumettes(self, nbre_allumettes):
        if nbre_allumettes <= self.nbre_max and nbre_allumettes < self.nbre_allumettes:
            self.nbre_allumettes -= nbre_allumettes
            self.perdant = 'Ordinateur'
            return True
        else:
            return False

    def tourOrdinateur(self):
        nbre_allumettes = randint(1, self.nbre_allumettes-1)

        while nbre_allumettes >= self.nbre_allumettes or nbre_allumettes > self.nbre_max:
            nbre_allumettes = randint(1, self.nbre_max - 1)

        self.nbre_allumettes -= nbre_allumettes
        self.perdant = 'Joueur'

    def verifierDerniereAllumette(self):
        if self.nbre_allumettes == 1:
            return True
        else:
            return False
