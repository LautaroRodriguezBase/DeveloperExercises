#Python 3.9.6

import numpy as R

filasMatriz = 5
columnasMatriz = 5
cantDeNumerosEnSecuencia = 4-1

posFinal = []
posInicial = []

#Dependiendo de como se pasen las variables va a recorrer la matriz en un sentido o en el otro
def scanHorizontal(m5x5, Desde, Hasta, Limite, paso):

    for filas in range(filasMatriz):
    
        for columnas in range(Desde-1, Hasta-Limite, paso):
            
            x = int((paso**2)**0.5)
            while m5x5[filas][columnas] == (m5x5[filas][columnas+(x*paso)]-x):

                if x == cantDeNumerosEnSecuencia:
            
                    posInicial.insert(0, [filas, columnas])
                    posFinal.insert(0, [filas, columnas+(x*paso)])
                    break
                x+=1

def scanVertical(m5x5, Desde, Hasta, Limite, paso):

    for columnas in range(columnasMatriz):
    
        for filas in range(Desde-1, Hasta-Limite, paso):
            x = int((paso**2)**0.5)
            while m5x5[filas][columnas] == (m5x5[filas+(x*paso)][columnas]-x):

                if x == cantDeNumerosEnSecuencia:
            
                    posInicial.insert(0, [filas, columnas])
                    posFinal.insert(0, [filas+(x*paso), columnas])
                    break
                x+=1

def main():

    matriz = R.random.randint(1, 6, size=(filasMatriz, columnasMatriz))

    # Se envia:
        # m5x5 = la matriz,
        # Desde = el numero desde que parte,
        # Hasta = el numero hasta el que va,
        # Limite = el numero que se le resta al anterior para que la matriz no se salga de rango,
        # Paso = el paso para recorrer la matriz
    scanHorizontal(matriz, 1, columnasMatriz, cantDeNumerosEnSecuencia, 1)
    scanHorizontal(matriz, columnasMatriz, cantDeNumerosEnSecuencia, 1, -1)

    scanVertical(matriz, 1, filasMatriz, cantDeNumerosEnSecuencia, 1)
    scanVertical(matriz, filasMatriz, cantDeNumerosEnSecuencia, 1, -1)
    
    print("""
{}
    posiciones Iniciales: {}
    posiciones Finales:   {}
    """.format(matriz, posInicial, posFinal))

main()