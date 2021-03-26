import random
import math


def media(x):
    return sum(x) / len(x)

def varianza(x):
    mu = media(x)

    acumulador = 0
    for x_ in x:
        acumulador += (x_ - mu)**2

    return acumulador / len(x)

def desviacion_estandar(x):
    return math.sqrt(varianza(x))