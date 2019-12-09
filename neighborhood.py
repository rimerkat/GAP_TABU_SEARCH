#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import neighbor as nb

class Neighborhood:
	"""
	Classe définissant l'ensemble des solutions voisines à une
	solution donnée.
	-Une solution est un dictionnaire dont les clés correspondent aux vols et les valeurs
	aux portes affectées à ces vols (p.e: solution{1:2, 2:1})
	-L'ensemble de solutions voisines est une liste des voisins (classe Neighbor), où chaque voisin est défini par un dictionnaire (solution
	voisine) et les mouvements qui ont généré ce voisin. """

	import random
	import tabu_list as tls

	""" Les attributs d'une instance de voisinage sont, respectivement, les suivants:
		- Nombre de vols du problème
		- Nombre de portes du problème
		- La solution courante de l'algorithme de Recherche Tabou pour laquelle on calcule les voisins
		- L'ensemble de voisinage de la solution courante (dernièrement calculé)
		- Les contraintes de compatibilité de portes-vols, correspondant à un dictionnaire dont les clés
			sont les vols. La valeur d'une clé est une liste de portes compatibles. Un exemple de contrainte
			est constr{1:[1], 2:[1,2]}. """

	def __init__(self, num_flights, num_gates, compatibilities):
		self.num_flights = num_flights
		self.num_gates = num_gates
		self.compatibilities = compatibilities

	def init_params(self, sol, tabu_list, iteration):
		self.current_solution = sol
		self.neighborhood = list()
		self.tabu_list = tabu_list
		self.iteration = iteration

	""" ** Méthode 1 de voisinage: affecter une nouvelle porte à chaque vol, pour toutes les portes, compte tenu la contrainte
		de compatibilité des portes aux vols. La fonction génère seulement les voisins non tabous. 
		Le voisinage est stocké dans la variable interne 'self.neighborhood'. ** """
	def generate_neighborhood_one(self):
		for f in range(self.num_flights):
			for g in range(self.num_gates):
				if (self.current_solution[f] is not g) and (self.is_gate_compatible(g,f)) and (not self.tabu_list.is_tabu(f,self.current_solution[f],g,self.iteration)):
					neighbor_dict = self.current_solution.copy()
					neighbor_dict[f] = g
					# une fois une solution voisine est générée, on stocke le mouvement qui l'a générée
					neighbor_ins = nb.Neighbor(neighbor_dict, f, self.current_solution[f], g)
					self.neighborhood.append(neighbor_ins)

	#""" Méthode 2: échanger les portes affectés à chaque paire de vols (sans contraintes). -- pas utilisée"""
	#def generate_neighborhood_swap(self):
	#	for f1 in range(self.num_flights):
	#		for f2 in range(self.num_flights):
	#			if f2 > f1:
	#				neighbor = self.current_solution.copy()
	#				self.swap_flights(neighbor,f1,f2)
	#				self.neighborhood.append(neighbor)

	""" ** Méthode 2: échanger les portes affectés à chaque paire de vols, compte tenu la contrainte
		de compatibilité des portes aux vols. La fonction génère seulement les voisins non tabous. ** """
	def gen_neighborhood_compatible_swap(self):
		for f1 in range(self.num_flights):
			for f2 in range(self.num_flights):
				if (f2 > f1) and (self.current_solution[f1] is not self.current_solution[f2]) and self.are_flights_compatible(self.current_solution,f1,f2) and (not self.tabu_list.is_tabu(f1,self.current_solution[f1],self.current_solution[f2],self.iteration)) and (not self.tabu_list.is_tabu(f2,self.current_solution[f2],self.current_solution[f1],self.iteration)):

					neighbor_dict = self.current_solution.copy()
					neighbor_ins = self.swap_flights(neighbor_dict,f1,f2) # échanger les portes de f1 et f2
					self.neighborhood.append(neighbor_ins)
					#print(neighbor_dict)
					#print("vol ",neighbor_ins.f1,"swap avec vol ",neighbor_ins.f2)
					#print("de porte ",neighbor_ins.old_gate_f1,"à porte ",neighbor_ins.new_gate_f1)


	""" ** Réinitialiser l'ensemble de voisinage déjà calculé. ** """
	def reset_neighborhood(self):
		self.neighborhood = list()

	# Fonctions internes

	""" ** Echanger les portes de deux vols ** """
	def swap_flights(self,solution,f1,f2):
		old_gf1 = solution[f1]
		solution[f1] = solution[f2]
		solution[f2] = old_gf1
		neighbor_ins = nb.Neighbor(solution, f1, old_gf1, solution[f1])
		neighbor_ins.add_swap(f2, solution[f1], old_gf1)

		return neighbor_ins

	""" ** Vérifier la contrainte de compatibilité d'une porte pour un vol ** """
	def is_gate_compatible(self,gate,flight):
		comp_vals = [c for c in self.compatibilities.values()]
		if gate in comp_vals[flight]: return True
		return False

	""" ** Vérifier la possiblité d'échanger les portes de deux vols ** """
	def are_flights_compatible(self,solution,f1,f2):
		gate_f1 = solution[f1]
		gate_f2 = solution[f2]
		if self.is_gate_compatible(gate_f1,f2) and self.is_gate_compatible(gate_f2,f1):
			return True
		return False

	""" Générer les voisins candidats en choisissant une des méthodes vues ci-dessus. """
	def generate_candidates(self, swap):
		if not swap:
			self.generate_neighborhood_one()
		else:
			self.gen_neighborhood_compatible_swap()

		return self.neighborhood

	# Le code ci-dessous attribue une porte aléatoire à chacun des vols,
	# tout en étant différente de la porte de la solution.
	# Par contre, cette méthode génére que num_flights voisins -- Non utilisée.

	# random_flight = random.randint(0,self.num_flights-1)
	# random_gate = random.randint(0,self.num_gates-1)

	# for (f,g) in self.current_solution:
	#     while not random_gate = g:
	#         random_gate = random.randint(0,self.num_gates-1)
	#     neighbor = np.copy(self.current_solution)
	#     neighbor[f] = random_gate
	#     self.neighborhood.append(neighbor)
