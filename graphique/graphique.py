#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graphique.telecran import Telecran
from graphique.cerclescolores import CerclesColores
from errors import *


class Graphique:

    def __init__(self):
        print('\nThème Graphique')
        self.choisirJeu()

    def afficherMenu(self):
        print('\n1 - Télécran\n2 - Cercles Colorés')
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
                    Telecran()
                elif choice == 2:
                    CerclesColores()
                else:
                    BadChoice()
            finally:
                if input('\nTaper q pour quitter le thème Graphique : ') == 'q':
                    break
        pass
