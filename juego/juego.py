from jugador import Jugador
from baraja import Baraja
import random


if __name__ == '__main__':

    mazo = Baraja()
    jugador1 = Jugador("Marco",mazo)
    jugador2 = Jugador("rival",mazo)


    while(jugador1.contador()<=21 and int(input('¿Pedir otra carta?: '))!= 1):

        jugador1.pedir_carta()
        print("jugador1",jugador1.get_mano())

        if(jugador1.contador()>21):
            print("GAME OVER")




        

