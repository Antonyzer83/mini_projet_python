#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NoInt:

    def __init__(self):
        print('\nLa valeur entrée n\'est pas un entier !')


class NoFloat:

    def __init__(self):
        print('\nLa valeur entrée n\'est pas un flottant !')

class BadChoice:

    def __init__(self):
        print('\nLe choix n\'existe pas !')


class BadVerification:

    def __init__(self):
        print('\nLa vérification a échouée : la valeur entrée est incorrecte !')
