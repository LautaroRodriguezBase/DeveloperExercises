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

    errorRadio = """Ups! El numero no debe:
    -ser menor o igual a 0(cero) 
    -contener caracteres distintos de 0 a 9
    -o tener mas de un '.'(punto)"""
    caracteresValidos = list((range(0, 10)))
    caracteresValidos += "."
    val = False

    for char in rad:

        if (char in str(caracteresValidos)) and not(rad.count(".") > 1):

            if float(rad) > 0:
                val = True
            else:
                print(errorRadio)
                return False    
        else:
            print(errorRadio)
            return False

    print("Calculando...")
    return val
            
def crearObjeto(rad):

    circuloMul = 1
    circuloNum = 0
    circulos = []

    rad = float(rad)

    circulos += [Circulo(rad)]

    circulos[circuloNum].areaCirculo()
    circulos[circuloNum].perCirculo()

    while True:

        if input("Desea cambiar el radio? y/n: ") == 'y':

            while True:
                rad = input("Radio del circulo: ")
                if radioEsValido(rad):

                    circulos[circuloNum].radio = float(rad)
                    circulos[circuloNum].areaCirculo()
                    circulos[circuloNum].perCirculo()
                    break
                
        elif input("Desea multiplicar el radio? y/n: ") == 'y':

            circuloNum += 1
            while True:
                circuloMul = input("Circulo * ")
                if radioEsValido(circuloMul):

                    rad = (float(rad) * float(circuloMul))

                    circulos += [Circulo(rad)]

                    circulos[circuloNum].areaCirculo()
                    circulos[circuloNum].perCirculo()
                    break
        else:
            break

    for circulo in circulos:
        print(circulo.radio)
        
def main():

    radio = input("Radio del circulo: ")

    if radioEsValido(radio):
        
        crearObjeto(radio)
    else:
        main()

main()