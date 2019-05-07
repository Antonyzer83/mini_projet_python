#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


class Divination:
    cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    symboles = ['Pique', 'Coeur', 'Trèfle', 'Carreau']
    first_card = [''] * 2
    next_card = [''] * 2
    score = 0

    def __init__(self):
        print('\nJeu Divination')
        self.creationCarte(True)
        while True:
            self.afficherCarte()
            choice = input('Plus ou moins : ')
            if self.verifierSigne(choice):
                self.score += 10
                print('Bravo !', self.next_card)
                self.creationCarte(False)
            else:
                print('\nVous avez perdu !\nVotre score :', self.score, self.next_card)
                break
        pass

    def creationCarte(self, Option):
        if Option:
            self.first_card[0] = self.cards[randint(0, len(self.cards)-1)]
            self.first_card[1] = self.symboles[randint(0, len(self.symboles)-1)]

        else:
            self.first_card[0] = self.next_card[0]
            self.first_card[1] = self.next_card[1]

        self.next_card[0] = self.cards[randint(0, len(self.cards)-1)]
        self.next_card[1] = self.symboles[randint(0, len(self.symboles)-1)]

        while self.next_card[0] == self.first_card[0]:
            self.next_card[0] = self.cards[randint(0, len(self.cards)-1)]
        pass

    def afficherCarte(self):
        print(self.first_card, 'Score :', self.score)
        pass

    def verifierSigne(self, signe):
        if signe == '+' and self.first_card[0] < self.next_card[0] or signe == '-' and self.first_card[0] > self.next_card[0]:
            return True
        else:
            return False
