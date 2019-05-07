#!/usr/bin/env python
# -*- coding: utf-8 -*-

from errors import *


class Mathematiques:
    unites = ["F", "f", "C", "c", "K", "k"]
    unite_depart = None
    unite_fin = None
    valeur = None

    def __init__(self):
        while True:
            print('\nThème Mathématiques\n\nJeu Conversion de Températures')
            print('\nUnités disponibles : Farenheit, Celcius, Kelvin (F,f,C,c,K,k).')

            unite_depart = input('Entrer l\'unité de départ : ')
            if self.verifierUnite(unite_depart):
                unite_fin = input('Entrer l\'unité de fin : ')
                if self.verifierUnite(unite_fin):
                    try:
                        valeur = int(input('Entrer la valeur à convertir : '))
                    except TypeError:
                        NoInt()
                        break
                    self.unite_depart = unite_depart
                    self.unite_fin = unite_fin
                    self.valeur = valeur
                    print('La valeur finale est égale à', self.convertir(), '.')
                    if input('\nTaper q pour quitter le thème Mathématiques : ') == 'q':
                        break
                else:
                    BadVerification()
            else:
                BadVerification()
        pass

    def verifierUnite(self, unite):
        if unite in self.unites:
            return True
        else:
            return False

    def convertir(self):
        if (self.unite_depart == "F" or self.unite_depart == "f") and (self.unite_fin == "C" or self.unite_fin == "c"):
            return (self.valeur - 32) * 5 / 9
        elif (self.unite_depart == "F" or self.unite_depart == "f") and (self.unite_fin == "K" or self.unite_fin == "K"):
            return (self.valeur - 32) * 5 / 9 + 273.15
        elif (self.unite_depart == "C" or self.unite_depart == "c") and (self.unite_fin == "F" or self.unite_fin == "f"):
            return (self.valeur * 9 / 5) + 32
        elif (self.unite_depart == "C" or self.unite_depart == "c") and (self.unite_fin == "K" or self.unite_fin == "k"):
            return self.valeur + 273.15
        elif (self.unite_depart == "K" or self.unite_depart == "k") and (self.unite_fin == "F" or self.unite_fin == "f"):
            return (self.valeur - 273.15) * 9 / 5 + 32
        elif (self.unite_depart == "K" or self.unite_depart == "k") and (self.unite_fin == "C" or self.unite_fin == "c"):
            return self.valeur - 273.15
        else:
            BadVerification()
            pass
