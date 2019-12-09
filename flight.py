import numpy as np 
import os

class Flight:
    """Classe définissant un vol, caractérisé par :
    - son numéro
    - son heure d'arrivée
    - son heure de départ
    - les portes sur lesquelles il peut attérir
    - sa contribution 
    - la porte qui lui est attribuée
	- attribut pour heuristique LIFO """


    def __init__(self):
        self.number = 0
        self.arrival_time = int(0)
        self.departure_time = int(100)
        self.compatible_gates = []
        self.contribution = 0
        self.gate = int(9999)
        self.assigned = False
