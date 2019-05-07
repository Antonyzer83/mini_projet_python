#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jeux.jeux import Jeux
from graphique.graphique import Graphique
from mathematiques.mathematiques import Mathematiques
from errors import *


class Application:
    """
        Première classe de l'application
        Gère le choix du thème
    """

    def afficherMenu(self):
        """
            Affiche le menu
        """
        print('\nBienvenue\n1 - Jeux\n2 - Graphique\n3 - Mathématiques')
        pass

    def choisirTheme(self):
        """
            Choix du thème et appel de classes de Thèmes
        """
        while True:
            self.afficherMenu()
            try:
                choice = int(input('\nEntrer votre choix : '))
            except TypeError:
                NoInt()
                break
            if choice == 1:
                Jeux()
            elif choice == 2:
                Graphique()
            elif choice == 3:
                Mathematiques()
            else:
                BadChoice()
            if input('\nTaper q pour quitter l\'application : ') == 'q':
                break
        pass
