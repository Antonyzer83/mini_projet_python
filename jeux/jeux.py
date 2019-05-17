#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jeux.allumettes import Allumettes
from jeux.divination import Divination
from jeux.jackpot import JackPot
from errors import *


class Jeux:

    def __init__(self):
        print('\nThème Jeux')
        self.choisirJeu()

    def afficherMenu(self):
        print('\n1 - Allumettes\n2 - Divination\n3 - Jack Pot')
        pass

    def choisirJeu(self):
        while True:
            self.afficherMenu()
            try:
                choice = int(input('\nEntrer votre choix : '))
            except ValueError:
                NoInt()
            else:
                if choice == 1:
                    Allumettes()
                elif choice == 2:
                    Divination()
                elif choice == 3:
                    JackPot()
                else:
                    BadChoice()
            finally:
                if input('\nTaper q pour quitter le thème Jeux : ') == 'q':
                    break
