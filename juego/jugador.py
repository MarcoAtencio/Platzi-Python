from baraja import Baraja

class Jugador:
    def __init__(self,nombre,baraja):
        self.nombre = nombre
        self.baraja = baraja
        self.mano = []

    def get_name(self):
        return self.nombre

    def get_mano(self):
        return self.mano

    def pedir_carta(self):
        self.mano.append(self.baraja.repartir())

    def contador(self):
        aux = 0
        for x in range(len(self.mano)):
            if(self.mano[x][1] == "A"):
                aux += 1
            
            elif(self.mano[x][1] == "J"):
                aux += 11

            elif(self.mano[x][1] == "Q"):
                aux += 12

            elif(self.mano[x][1] == "K"):
                aux += 13

            else:
                aux += int(self.mano[x][1])
                
        return aux
        

