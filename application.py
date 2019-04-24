#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jeux.jeux import Jeux
from graphique.graphique import Graphique
from mathematiques.mathematiques import Mathematiques
from errors import *


class Application:

    def afficherMenu(self):
        print('\nBienvenue\n1 - Jeux\n2 - Graphique\n3 - Mathématiques')
        pass

    def choisirTheme(self):
        while True:
            self.afficherMenu()
            try:
                choice = int(input('\nEntrer votre choix : '))
                if choice == 1:
                    Jeux()
                elif choice == 2:
                    Graphique()
                elif choice == 3:
                    Mathematiques()
                else:
                    BadChoice()
            except:
                NoInt()
            if input('\nTaper q pour quitter le programme : ') == 'q':
                break
        pass
