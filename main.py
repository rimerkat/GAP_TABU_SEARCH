#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import data
import tabu
import neighborhood as nbhd
import fonctionm as fm


filename = "data/GAP5_25"
n_flights = 25
n_gates = 5

""" Lire les données d'une instance du problème """
flights, compatibilities, L0, LNP1 = data.read_instance(filename)

""" Créer une instance Tabu """
tabu_ins = tabu.Tabu(n_flights,n_gates,compatibilities, flights, L0, LNP1)

""" 1-Choisir la méthode de voisinage pour lancer l'algorithme """
#SWAP = True	# méthode de voisinage SWAP activée (True) ou pas (False)
SWAP = False

""" 2-Choisir si la solution initiale est aléatoire ou fixe """
#RANDOM = True
RANDOM = False

""" 3-Choisir le nombre maximum d'itérations """
KMAX = 100
#KMAX = 300
#KMAX = 600

""" Lancer l'algorithme de Recherche Tabou """
tabu_ins.start_search(SWAP,RANDOM, KMAX)


