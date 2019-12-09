
# Fonction qui prend en argument une porte et le vecteur des vols
#et qui revoit un vecteur qui contient tous les vols assignés
# à cette porte par ordre croissant de temps d'arrivée

def flights_assigned(gate, flights):
    """ Renvoit le tableau de vols assignées à porte passée en argument"""
    FlightsOnGate = []
    for i in range(len(flights)):
        if flights[i].gate == gate:
            FlightsOnGate.append(flights[i])
    return FlightsOnGate

# Fonction qui renvoie la position du vol flight i dans la porte j 
 # cette fonction est valide et utilisable que dans le cas ou le vol i est dans la porte j
 
def position_flight_gate(flight_i,gate_j,flights):
    FlightsOnGate_j = flights_assigned(gate_j,flights)
    indice = 0
    for k in range(len(FlightsOnGate_j)):
        if FlightsOnGate_j[k]==flight_i:
            indice=k
    return indice            


# Fcontion qui calcule la contribution de chaque vol

def contribution(flight_i,flights,L0):
    delta=0
    gate_j=flight_i.gate
    #print(gate_j)
    FlightsOnGate = flights_assigned(gate_j,flights)
    index=position_flight_gate(flight_i,gate_j,flights)
    #print(index)
    if index == 0:
        delta=(flight_i.arrival_time - L0)**2
    
    flight_avant_i=FlightsOnGate[index-1]
    #print(flight_avant_i.number)
    #print(flight_avant_i.departure_time)
    if flight_avant_i.departure_time <= flight_i.arrival_time :
        delta = (flight_i.arrival_time-flight_avant_i.departure_time)**2
    return delta

# Fonction qui calcul le dernier temps d'inactivité au carré dans chaque porte 
# car il n'est pas pris dans les contribution

def contribution_fin_gate(gate_i,flights,LNP1):
    delta=0
    FlightsOnGate= flights_assigned(gate_i,flights)
    last_flight = FlightsOnGate[len(FlightsOnGate)-1]
   # print(last_flight.number)
    delta=LNP1 - last_flight.departure_time
    return delta**2    
    
## Fonction qui calcul la somme carré des temps d'inactivités

def contribution_total(flights,n_gates,L0,LNP1):
    c=0
    d=0
    for i in range(len(flights)):
        c=c+contribution(flights[i],flights,L0) 
    for gate in range(n_gates):
        d=d+ contribution_fin_gate(gate,flights,LNP1)
    return c+d

# Fonction qui definit si deux flights sont en conflit d'horaire ou non 
def conflit(flight_i,flight_j):
    c=1
    if flight_i.departure_time <= flight_j.arrival_time:
        c=0
    if flight_j.departure_time <= flight_i.arrival_time:
        c=0  
    return c



def conflit_same_gate(flight_i,flight_j):
    d=0
    c=conflit(flight_i,flight_j)
    if flight_i != flight_j:
        if flight_i.gate==flight_j.gate:
            d=c
    return d

def conflit_total(flights):
    c=0
    Kc=1500
    for i in range(len(flights)):
        for j in range(len(flights)):
            c=c+conflit_same_gate(flights[i],flights[j])
    return Kc*c/2

def fonction_objectif(flights,n_gates,L0,LNP1):
	Kc=1500
	c=contribution_total(flights,n_gates,L0,LNP1)
	d=conflit_total(flights)
	res=c+d

	return res, d/Kc

# Fonction  qui crée un vecteur qui contient les flights qui sont en conflits 
# avec un flight i et qui sont dans une porte Gate

def find_flights_conflit(flight_i,gate_j,flights):
    vecteur_flights_conflit =[]
    FlightsOnGate=flights_assigned(gate_j,flights)
    for i in range (len( FlightsOnGate)):
        if conflit(flight_i,FlightsOnGate[i])==1:
            if flight_i!=FlightsOnGate[i]:
                vecteur_flights_conflit.append(FlightsOnGate[i])
    return vecteur_flights_conflit

# fonction qui calcule la partie a ajouter ou a retrancher au dèbut si ça existe 
def partie_debut(flight_i,gate_j,flights):
    delta=0
    flights_conflit = find_flights_conflit(flight_i,gate_j,flights)
    if len(flights_conflit)!=0:
        first_flight_conflit=flights_conflit[0]
        if flight_i.arrival_time < first_flight_conflit.arrival_time:
            delta=(first_flight_conflit.arrival_time - flight_i.arrival_time )
    return delta

# fonction qui calcule la partie a ajouter ou a retrancher à la fin si ça existe        
def partie_fin(flight_i,gate_j,flights):       
    delta=0
    flights_conflit = find_flights_conflit(flight_i,gate_j,flights)
    if len(flights_conflit)!=0:
        last_flight_conflit=flights_conflit[len(flights_conflit)-1]
        if flight_i.departure_time >  last_flight_conflit.departure_time:
            delta=(flight_i.departure_time - last_flight_conflit.departure_time )
    return delta

# fonction qui calcule la somme des carré des temps d'inactivité à rajouter 
# ou retrancher au milieu des vols en conflits

def partie_milieu(flight_i,gate_j,flights):
    delta=0
    flights_conflit = find_flights_conflit(flight_i,gate_j,flights)
    if len(flights_conflit)!=0:
        for i in range(len(flights_conflit)-1):
            if conflit(flights_conflit[i],flights_conflit[i+1])==0:
                gamma= flights_conflit[i+1].arrival_time - flights_conflit[i].departure_time
                delta=delta+gamma**2
    return delta


#def cout_enlever(flight,gate):
#    cout=0
#    FlightsOnGate = flights_assigned(gate)
#    index=position_flight_gate(flight,FlightsOnGate)
#    flight_conflit = find_flights_conflit(flight,gate)
#    if flight_conflit=[]:
#        if index <
#            cout=contribution(Flight)+contribution(FlightsOnGate[index+1])
        
            
            




         




          
               
           
           
