#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:44:15 2019

@author: hbsbh1
"""
import data_problemem
import fonctionm

data = data_problemem.Data("GAP5_25", 25, 5)

print("**** Heuristique LIFO ****")
#data.LIFO()
#data.display_problem_data()

data.flights[0].gate=4
data.flights[1].gate=2
data.flights[2].gate=1
data.flights[3].gate=4
data.flights[4].gate=4
data.flights[5].gate=4
data.flights[6].gate=3
data.flights[7].gate=1
data.flights[8].gate=4
data.flights[9].gate=1
data.flights[10].gate=4
data.flights[11].gate=1
data.flights[12].gate=4
data.flights[13].gate=2
data.flights[14].gate=2
data.flights[15].gate=2
data.flights[16].gate=0
data.flights[17].gate=4
data.flights[18].gate=3
data.flights[19].gate=4
data.flights[20].gate=4
data.flights[21].gate=0
data.flights[22].gate=3
data.flights[23].gate=2
data.flights[24].gate=1


A= fonctionm.flights_assigned(0, data.flights)
#Affichage de la séquence d'avions à ordonnancer."""  
print("*** Vols dans la porte 0 ***")
for i in range(len(A)):
    print("Vol ", A[i].number, 
        " : Heure d'arrivée = ", A[i].arrival_time,
        " --- Heure de départ = ", A[i].departure_time, 
        " --- Porte assignée = ", A[i].gate, sep="")
    
B= fonctionm.flights_assigned(1, data.flights)
#Affichage de la séquence d'avions à ordonnancer."""  
print("*** Vols dans la porte 1***")
for i in range(len(B)):
    print("Vol ", B[i].number, 
        " : Heure d'arrivée = ", B[i].arrival_time,
        " --- Heure de départ = ", B[i].departure_time, 
        " --- Porte assignée = ", B[i].gate, sep="")
    
    
C= fonctionm.flights_assigned(2, data.flights)
#Affichage de la séquence d'avions à ordonnancer."""  
print("*** Vols dans la porte 2***")
for i in range(len(C)):
    print("Vol ", C[i].number, 
        " : Heure d'arrivée = ", C[i].arrival_time,
        " --- Heure de départ = ", C[i].departure_time, 
        " --- Porte assignée = ", C[i].gate, sep="")    


D= fonctionm.flights_assigned(3, data.flights)
#Affichage de la séquence d'avions à ordonnancer."""  
print("*** Vols dans la porte 3***")
for i in range(len(D)):
    print("Vol ", D[i].number, 
        " : Heure d'arrivée = ", D[i].arrival_time,
        " --- Heure de départ = ", D[i].departure_time, 
        " --- Porte assignée = ", D[i].gate, sep="")   


E= fonctionm.flights_assigned(4, data.flights)
#Affichage de la séquence d'avions à ordonnancer."""  
print("*** Vols dans la porte 4***")
for i in range(len(E)):
    print("Vol ", E[i].number, 
        " : Heure d'arrivée = ", E[i].arrival_time,
        " --- Heure de départ = ", E[i].departure_time, 
        " --- Porte assignée = ", E[i].gate, sep="") 
    
#index=fonctionm.position_flight_gate(data.flights[12],1,data.flights)
#print(index)
L0=100
#c=0
#for i in range(len(data.flights)):
 #  print("vol",data.flights[i].number,fonctionm.contribution(data.flights[i],data.flights,L0))
  # c=c+fonctionm.contribution(data.flights[i],data.flights,L0)
    
#print(c)
    
#cont=fonctionm.contribution(data.flights[1],data.flights,L0)
#print(cont)
LNP1=215
#contr=fonctionm.contribution_fin_gate(2,data.flights,LNP1)
#print(contr)

gates=[0,1,2,3,4]
#contribution=fonctionm.contribution_total(data.flights,gates,L0,LNP1)
#print(contribution)


#print(data.flights[20].gate)

#for i in range(len(gates)):
    #print(fonctionm.contribution_fin_gate(gates[i],data.flights,LNP1))
    #c=c+fonctionm.contribution(data.flights[i],data.flights,L0)
#print(c)
#c=fonctionm.contribution(data.flights[20],data.flights,L0)
#print (c)
    
    
#c=fonctionm.conflit(data.flights[16],data.flights[19])  
#print(c)

#c=fonctionm.conflit_same_gate(data.flights[10],data.flights[11])  
#print(c)  
       
#c=0
#for i in range(len(data.flights)):
 #       for j in range(len(data.flights)):
  #          c=fonctionm.conflit_same_gate(data.flights[i],data.flights[j])
   #         print(data.flights[i].number,data.flights[j].number,c)

#c=fonctionm.conflit_total(data.flights)    
#print("nombre de conflit ",c)        

#d=fonctionm.contribution_total(data.flights,gates,L0,LNP1)
#print("somme temps inactivitées",d) 

#obj=fonctionm.fonction_objectif(data.flights,gates,L0,LNP1)   
#print("fonction objectif ",obj)
   

#vect=fonctionm.find_flights_conflit(data.flights[13],2,data.flights)   

#print("*** conflits de 4 ***")
#for i in range(len(vect)):
 #  print("Vol ", vect[i].number, 
  #      " : Heure d'arrivée = ", vect[i].arrival_time,
   #     " --- Heure de départ = ", vect[i].departure_time, 
    #    " --- Porte assignée = ", vect[i].gate, sep="")
"""cout_enlever=fonctionm.cout_enlever(data.flights[20],4,data.flights,L0,LNP1)
print("cout = ",cout_enlever)

ff=FlightsOnGate = fonctionm.flights_assigned(4,data.flights)
ii=index=fonctionm.position_flight_gate(data.flights[20],4,data.flights) 
print(ii)
a=fonctionm.contribution(data.flights[20],data.flights,L0)
print("a = ",a)
b=fonctionm.partie_debut(data.flights[20],4,data.flights)
print("b = ",b)
#c=fonctionm.contribution(FlightsOnGate[index+1],data.flights,L0)
#print("c = ",c)
d=fonctionm.partie_fin(data.flights[20],4,data.flights)
print("d = ",d)
e=fonctionm.partie_milieu(data.flights[20],4,data.flights)
print("e = ",e)
#cout=(a+b)**2-a**2+(c+d)**2-c**2+e
#print("cout = ",cout)

flight_conflit = fonctionm.find_flights_conflit(data.flights[20],4,data.flights)
print(len(flight_conflit))"""

   
#FlightsOnGate = fonctionm.flights_assigned(3,data.flights)   
#p=fonctionm.position(data.flights[24],3,data.flights)
#print(p)
 
#cout_ajouter=fonctionm.cout_ajouter(data.flights[13],3,data.flights,L0,LNP1)
#print(cout_ajouter)
 
#i=fonctionm.position_fictive(data.flights[12],1,data.flights)
#print(i)
#aph=fonctionm.cout_ajouter(data.flights[8],3,data.flights,L0,LNP1)
#print(aph)
delta=fonctionm.delta_evaluation(data.flights[5],data.flights[18],data.flights,L0,LNP1,1000)
print(delta)