#Python 3.9.6

import math

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

    errorRadio = """Ups! El radio no debe:
    -ser menor o igual a 0(cero) 
    -contener caracteres distintos de 0 a 9
    -o tener mas de un '.'(punto)"""
    caracteresValidos = list((range(1, 10)))
    caracteresValidos += "."
    val = False

    for char in rad:

        if (char in str(caracteresValidos)) and not(rad.count(".") > 1):
            val = True
        else:
            print(errorRadio)
            return False

    print("Calculando...")
    return val
            

def crearObjeto(rad):

    circulo1 = Circulo(rad)

    circulo1.areaCirculo()
    circulo1.perCirculo()

    if input("Desea cambiar el radio? y/n: ") == 'y':

        main()

def main():

    radio = input("Radio del circulo: ")

    if radioEsValido(radio):
        
        crearObjeto(float(radio))
    else:
        main()


main()