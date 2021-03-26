import random
import copy

class Baraja:
    def __init__(self):
        self.caras = ['espada', 'corazon', 'rombo', 'trebol']
        self.valores = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cartas = self.crear_baraja()


    def crear_baraja(self):
        barajas = []
        for cara in self.caras:
            for valor in self.valores:
                    barajas.append((cara,valor))   
        return random.sample(barajas,52)

    def get_size(self):
        return len(self.cartas)-1

    def get_mazo(self):
        return self.cartas

    def repartir(self):
        aux = copy.copy(self.cartas[self.get_size()])
        self.cartas.pop(self.get_size())
        return aux

    def contador_cuartetos(self):
        aux = [(0,'A'), (0,'2'), (0,'3'), (0,'4'), (0,'5'), (0,'6'), (0,'7'), (0,'8'), (0,'9'), (0,'10'), (0,'J'), (0,'Q'), (0,'K')]
        aux = list(map(list,aux))
        for valor in range(len(self.valores)):
            for x in range(self.get_size()+1):
                if(self.valores[valor] == self.cartas[x][1]):
                    aux[valor][0] = aux[valor][0] + 1
        return aux