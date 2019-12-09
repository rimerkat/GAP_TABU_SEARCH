#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tabu_list:
    """Classe définissant une liste tabou
    La liste est structurée avec un dictionnaire appelé "tabu"
    ***
    - Les clés du dictionnaire sont le tuple (avion i, gate k, gate l)
    - Les valeurs correspondent à la valeur de l'itération n à laquelle 
    le mouvement a été créé comme tabou plus la durée de vie du mouvement d
    ***
    Par exemple, si le changement de porte 0 vers 2 sur l'avion 1 
    est interdit lors de la première itération, on aura :
    {(1, 0, 2) : d+1 }
    """

    def tabu_list_creation(self):
        self.list = dict()

    def insert_movement(self, plane, gate1, gate2, i):
        self.list[(plane, gate1, gate2)] = i + self.duration

    def del_movement(self, plane, gate1, gate2):
        del self.list[(plane, gate1, gate2)]

    def is_tabu(self, plane, gate1, gate2, i):
        if (plane, gate1, gate2) in self.list.keys() and i <= self.list[(plane, gate1, gate2)]:
            return True
        else :
            if (plane, gate1, gate2) in self.list.keys() and i > self.list[(plane, gate1, gate2)]:
                self.del_movement(plane, gate1, gate2)
            return False

    def tabu_cleaning(self, i):
        tabu_to_clean = [movements for movements in self.list.keys()]
        for movements in tabu_to_clean:
            if i > self.list[movements]:
                self.del_movement(movements[0], movements[1], movements[2])


    def __init__(self, d):
        self.tabu_list_creation()
        self.duration = d
