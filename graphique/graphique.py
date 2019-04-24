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
        self.afficherMenu()
        try:
            choice = int(input('\nEntrer votre choix : '))
            if choice == 1:
                Telecran()
                pass
            elif choice == 2:
                CerclesColores()
                pass
            else:
                BadChoice()
                pass
        except:
            NoInt()
            pass
