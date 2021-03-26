import random
import math
from estadistica import desviacion_estandar, varianza

def aventar_agujas(numero_agujas):
    adentro_circulo = 0

    for _ in range(numero_agujas)
        x = random.random * random.choice([-1,1])
        y = random.random * random.choice([-1,1])
        distancia_desde_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_centro <= 1:
            adentro_circulo +=1

        return (4 * adentro_circulo) / numero_agujas

def estimacion(numero_agujas, numero_intentos):
    estimados = []
    for _ in range(numero_intentos):
        estimacion_pi = aventar_agujas(numero_agujas)
        estimados.append(estimacion_pi)
        random.ra
    
    media_estimado = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Est={round(media_estimado,5)}, sigma={round(sigma,5)}, agujas={numero_agujas}')