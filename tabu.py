#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import data, random
import neighborhood as nbhd
import tabu_list as tls
import fonctionm as fm

#NB_ITERATIONS = 100	# nombre d'itérations de l'algorithme (condition d'arrêt)
TABU_DURATION = 10 # durée d'interdiction d'un mouvement dans la liste tabou

class Tabu:
	""" Classe définissant l'algorithme tabou et ses fonctions et éléments internes. """

	def __init__(self, n_flights, n_gates, compatible_constr, flights, L0, LNP1):
		#self.optimal_sol = dict()
		#self.optimal_value = 0.0
		self.n_gates = n_gates
		self.n_flights = n_flights
		self.compatibilities = compatible_constr
		self.flights = flights # vecteur de classe Flight
		self.L0 = L0
		self.LNP1 = LNP1


	""" ** Fonction définissant l'algorithme tabou ** """
	def start_search(self, SWAP, RANDOM, KMAX):

		# 0- Créér une instance de voisinage
		self.nb = nbhd.Neighborhood(self.n_flights,self.n_gates, self.compatibilities)

		print("\n LANCEMENT DE LA RECHERCHE TABOU ..")

		""" 1- Calculer la solution initiale et sa valeur objectif """
		if not RANDOM:
			sol = self.initial_solution_fixe() # partir d'une solution initiale fixe
		else:
			sol = self.initial_solution() # partir d'une solution initiale aléatoire
		self.flights = self.dict_sol_to_vect_flights(sol) # convertir le format de solution de dict() à [Flight] pour affichage

		""" 2- Calculer sa valeur objectif et le nombre de conflicts dans la solution """
		value, conflict = self.objective_function(sol)

		""" 3- Enregistrer la solution optimale """
		self.optimal_sol = sol	
		self.optimal_value = value
		self.optimal_conflict = conflict

		print("Solution Initiale: ")
		self.display_solution(self.flights) # afficher la solution initiale
		print("Valeur initiale: ", self.optimal_value,)
		print("Nombre de conflicts initial: ",self.optimal_conflict,"\n")

		""" 4- Créer une liste Tabou """
		self.tabu_list = tls.Tabu_list(TABU_DURATION)

		self.iteration = 0

		""" 5- Commencer la recherche tabou jusqu'à atteindre la condition d'arrêt (nombre max d'itérations) """

		while self.iteration < KMAX: #NB_ITERATIONS:
			print("Iteration ",self.iteration)

			""" 5.1- Calculer l'ensemble de voisinage de la solution courante 'sol' qui ne sont pas tabous """
			self.nb.init_params(sol, self.tabu_list, self.iteration)
			candidates = self.nb.generate_candidates(SWAP) # la méthode SWAP peut être activée ou pas
			#print("On a ",len(candidates)," candidats")

			""" 5.2- Déterminer le meilleur candidat du voisinage non tabou (celui minimisant la fonction objectif) """
			# on garde sa valeur objectif, sa solution et le nombre de conflicts de la solution
			best_value, best_candidate, best_conf = self.best_solution(candidates) 

			#print("Meilleur candidat ",best_candidate.neighbor)
			#print(" a une valeur de ",best_value)

			#print("Le meilleur candidat est le swap du vol",best_candidate.f1," de porte ",best_candidate.old_gate_f1,"à ",best_candidate.new_gate_f1)
			
			""" 5.3- Mettre à jour la liste tabou """
			if best_value > value:
				self.add_tabu(best_candidate, SWAP)
				print("Liste tabou:",self.tabu_list.list)

			""" 5.4- Mettre à jour la solution et valeur optimales """
			if best_value < self.optimal_value:
				self.optimal_sol = best_candidate.neighbor
				self.optimal_value = best_value
				self.optimal_conflict = best_conf

				#print("Meilleure valeur jusque là est ",self.optimal_value)

			""" 5.5- Mettre à jour la solution courante """
			sol = best_candidate.neighbor
			value = best_value
			conflict = best_conf

			print("Coût de la solution courante: ",value)
			print("Nombre de conflicts: ",conflict)

			""" 6- Passer à l'itération suivante """
			self.iteration = self.iteration +1

		print("FIN RECHERCHE\n")

		optim_sol_flights = self.dict_sol_to_vect_flights(self.optimal_sol) # convertir format de solution finale pour affichage
		
		# afficher la solution optimale après la fin de la recherche
		self.display_solution(optim_sol_flights)
		print("de valeur optimale :",self.optimal_value)
		print("et de nombre de conflicts:",self.optimal_conflict)




	""" ****** Fonctions de manipulation de solutions ****** """

	def initial_solution(self):
		solution = dict()
		for flight in range(self.n_flights):
			random_gate = random.randint(0,self.n_gates-1)
			while not self.nb.is_gate_compatible(random_gate,flight):
			    random_gate = random.randint(0,self.n_gates-1)
			solution[flight] = random_gate
		return solution

	def initial_solution_fixe(self):
		flights = dict()
		flights[0]=4
		flights[1]=2
		flights[2]=1
		flights[3]=4
		flights[4]=4
		flights[5]=4
		flights[6]=3
		flights[7]=1
		flights[8]=4
		flights[9]=1
		flights[10]=4
		flights[11]=1
		flights[12]=4
		flights[13]=2
		flights[14]=2
		flights[15]=2
		flights[16]=0
		flights[17]=4
		flights[18]=3
		flights[19]=4
		flights[20]=4
		flights[21]=0
		flights[22]=3
		flights[23]=2
		flights[24]=1
	
		return flights

	""" ** Pour afficher une solution de format [Flight] (vecteur d'instances Flight) ** """
	def display_solution(self, sol_flights):
		for g in range(self.n_gates):
			print("Sur Porte ",g,":")
			for f in fm.flights_assigned(g,sol_flights):
				print("Vol ",f.number,": heure d'arrivée ",f.arrival_time," et heure de départ ",f.departure_time)


	""" ****** Fonctions internes ****** """

	""" ** Fonction qui calcule la fonction objectif ou coût d'une solution donnée.
		Elle retourne la valeur objectif et le nombre de conflicts trouvés entre les vols. ** """
	def objective_function(self, sol):
		# convertir format de solution
		flights = self.dict_sol_to_vect_flights(sol)
		# calculer sa valeur objectif
		obj, conflict = fm.fonction_objectif(flights, self.n_gates, self.L0, self.LNP1)
		return obj, conflict

	""" ** Fonction qui calcule la meilleur solution minimisant la fonction objectif sur un ensemble de solutions.
		Notamment pour calculer le meilleur voisin d'un voisinage. ** """
	def best_solution(self, sols): # sols est une liste de classes Neighbor
		i = 0
		result0, conflict0 = self.objective_function(sols[i].neighbor)
		best_sol = sols[i].neighbor
		best_pos = i
		while i < len(sols)-1:
			i = i+1
			new_res, new_conf = self.objective_function(sols[i].neighbor)
			if new_res < result0:
				best_sol = sols[i].neighbor
				result0 = new_res
				best_pos = i
				conflict0 = new_conf

		return result0, sols[best_pos], conflict0

	""" ** Fonction qui ajoute un mouvement à la liste tabou. Elle prend un voisin comme paramètre et interdit le mouvement qui a généré ce 		voisin. Par exemple, si un voisin est généré en changeant dans la solution originale la porte du vol 3 de porte 1 à 2,
		donc on dit que le mouvement qui a généré ce voisin est (vol 3, porte 1, porte 2). ** """
	def add_tabu(self, neighbor_ins, SWAP):
		self.tabu_list.insert_movement(neighbor_ins.f1, neighbor_ins.old_gate_f1, neighbor_ins.new_gate_f1, self.iteration)
		#print("Nouveau mouvement tabou ajouté: (Vol ",neighbor_ins.f1,": porte ",neighbor_ins.old_gate_f1,"=> porte ",neighbor_ins.new_gate_f1,")")

		if SWAP: # si la méthode de voisinage de swap est activée, on interdit aussi le mouvement du second vol (vol de swap)
			self.tabu_list.insert_movement(neighbor_ins.f2, neighbor_ins.old_gate_f2, neighbor_ins.new_gate_f2, self.iteration)
			print("Nouveau mouvement tabou ajouté: (Vol ",neighbor_ins.f2,": porte ", neighbor_ins.old_gate_f2,"=> porte ",neighbor_ins.new_gate_f2,")")


	""" ** Fonctions de support ** """

	#def get_iteration(self):
	#	return self.iteration

	#def get_tabu_duration(self):
	#	return TABU_DURATION

	#def get_tabu_list_length(self):
	#	return TABU_LIST_SIZE


	""" ** Fonction de conversion de format d'une solution (de dict() à vecteur de Flights) ** """
	def dict_sol_to_vect_flights(self, sol_dict):
		sol_flights = self.flights.copy()
		for i in range(self.n_flights):
			sol_flights[i].gate = sol_dict[i]
		return sol_flights
