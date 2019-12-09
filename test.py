import data 
import random
import neighborhood as nbhd
import tabu_list as tls
import fonctionm as fm

def initial_solution(num_flights, num_gates, constraint):
	solution = dict()
	for flight in range(num_flights):
		random_gate = random.randint(0,num_gates-1)
		#while constraint and not nbhd.is_gate_compatible(random_gate,flight):
		#    random_gate = random.randint(0,num_gates-1)
		solution[flight] = random_gate
	return solution

def display_solution(sol):
	print("solution{")
	for f in sol.keys():
		print("flight ",f," to gate ",sol[f])
	print("}")

sol = initial_solution(4,2,False)

def objective_function(sol):
	return sum(sol.values())#-sol[0]

val = objective_function(sol)
#display_solution(sol)

def best_solution(sols):
	i = 0
	result0 = objective_function(sols[i])
	best_sol = sols[i]
	while i < len(sols)-1:
		i = i+1
		new_res = objective_function(sols[i])
		if new_res < result0:
			best_sol = sols[i]
			result0 = new_res
	
	return result0, best_sol

bs = best_solution([{1:1,2:2},{1:1,2:1}])
print("bst sol: ",bs)

ls = tls.Tabu_list(2)

sol1 = {1:1,2:2}
def add_tabu(neighbor):
	for f in neighbor.keys():
		if neighbor[f] is not sol1[f]:
			ls.insert_movement(f,sol1[f],neighbor[f],0)

add_tabu({1:2,2:2})
print(ls.list)

# a partir d ici on teste fonction objectif

flights, compatibilities, L0, LNP1 = data.read_instance("data/GAP5_25")
sol_flights = flights.copy()
data.display_data(sol_flights)

random_gate = random.randint(0,2)
print(random_gate)


filename = "data/GAP5_25"
n_flights = 25
n_gates = 5

""" Lire les données d'une instance du problème """
flights, compatibilities, L0, LNP1 = data.read_instance(filename)
#print(compatibilities)

def is_gate_compatible(gate,flight,compatibilities):
	comp_vals = [c for c in compatibilities.values()]
	print(comp_vals)
	if gate in comp_vals[flight]: return True
	return False
print(is_gate_compatible(1,15,compatibilities))

