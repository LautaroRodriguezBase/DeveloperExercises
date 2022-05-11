#Python 3.9.6

import math
from re import T

class Circulo:


    def __init__(self, radio):

        self.radio = float(radio)
        self.nPi = math.pi

    def perCirculo(self):
        
        perimetro = 2*self.nPi*self.radio
        print("Perimetro:", perimetro)

    def areaCirculo(self):

        area = self.nPi*(self.radio**2)
        print("Area:", area)

def radioEsValido(rad):

    errorRadio = "Ups! El radio no debe ser menor o igual a 0(cero)"

    if rad <= 0:

        print(errorRadio)
        return False
    else:
        
        print("Calculando...")
        return True

def main():

    radio = float(input("Radio del circulo: "))

    if radioEsValido(radio):
        circulo1 = Circulo(radio)

        circulo1.areaCirculo()
        circulo1.perCirculo()

main()