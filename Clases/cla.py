#Python 3.9.6

import math

class Circulo:


    def __init__(self, radio):
        
        error = "Ups! No puedes ingresar un radio menor o igual a 1"

        if radio > 0:

            self.radio = float(radio)
            self.nPi = math.pi
        else:
            print(error)

    def perCirculo(self):
        
        perimetro = 2*self.nPi*self.radio
        print(perimetro)

    def areaCirculo(self):

        area = self.nPi*(self.radio**2)
        print(area)

radio = float(input("Radio del circulo: "))

circulo1 = Circulo(radio)

circulo1.areaCirculo()
circulo1.perCirculo()