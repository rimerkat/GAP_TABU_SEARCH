#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import os
import flight

flights = []
pb_data = dict()  #Dictionnary that contains number of flights N and gates M

def read_instance(filename):

	#====== VARIABLES INITIALIZATION =====

	A=list()
	A_h=list()
	A_m=list()
	D=list()
	D_h=list()
	D_m=list()
	L0 = 0
	LNP1 = 0
	P = dict()
	n=0

	#====== Data File reading ======
	
	with open(filename+'.txt', 'r') as file:
		all_data = file.read()
	
	#====== Data formating ======    
	
	line = all_data.split("\n")  #corresponds to each line of the data file

	for i in range(len(line)):
		if i==0 or i==1 :
			temp = line[i].split(" ")
			pb_data[temp[0]]= temp[1]
		else:                           #contruction of vectors A, D and matrix P
			temp = line[i].split(" ")
			if len(temp) > 1:
				A.append(temp[1])
				D.append(temp[2])
				P[n] = []
				for j in range(3, len(temp)-1):
					P[n].append(int(temp[j]))
				n+=1

	#====== Discrete time computation ======            

	for i in range(len(A)):
		A_split = str(A[i]).split(":")
		D_split = str(D[i]).split(":")
		A_h.append(A_split[0])
		A_m.append(A_split[1])
		D_h.append(D_split[0])
		D_m.append(D_split[1])
		A[i]= int(A_h[i])*12 + int(int(A_m[i])/5) 
		D[i]= int(D_h[i])*12 + int(int(D_m[i])/5) 

	L0 = int(A_h[0])*12
	LNP1 = (int(D_h[len(D)-1])+1) *12

	#======= Flight objects creation =======

	for i in range(int(pb_data["Flights"])):
		flights.append(flight.Flight())
		flights[i].number = i
		flights[i].arrival_time = A[i]
		flights[i].departure_time = D[i]
		flights[i].compatible_gates = P[i]

	return flights, P, L0, LNP1



	"""Affichage de la séquence d'avions à ordonnancer."""
def display_data(flights):
	print("*** Vols ***")
	for i in range(len(flights)):
		print("Vol ", flights[i].number,
			" : Heure d'arrivée = ", flights[i].arrival_time,
			" --- Heure de départ = ", flights[i].departure_time,
			" --- Portes compatibles = ", flights[i].compatible_gates,
			" --- Porte assignée = ", flights[i].gate, sep="")



