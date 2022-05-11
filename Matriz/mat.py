"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

#Python 3.9.6

import numpy as R

filasMatriz = 5
columnasMatriz = 5
cantDeNumerosEnSecuencia = 4-1

posFinal = []
posInicial = []

def scanHorizontal(m5x5):

    for filas in range(filasMatriz):
        
        for columnas in range(columnasMatriz-cantDeNumerosEnSecuencia):
            x = 1
            while m5x5[filas][columnas] == (m5x5[filas][columnas+x]-x):

                if x == 3:
            
                    posInicial.insert(0, [filas, columnas])
                    posFinal.insert(0, [filas, columnas+x])
                    break
                x+=1
    
    for filas in range(filasMatriz):
        
        for columnas in range(columnasMatriz-1, (cantDeNumerosEnSecuencia-1), -1):
            x = 1
            while m5x5[filas][columnas] == (m5x5[filas][columnas-x]-x):

                if x == 3:
            
                    posInicial.insert(0, [filas, columnas])
                    posFinal.insert(0, [filas, columnas-x])
                    break
                x+=1

def scanVertical(m5x5):

    for columnas in range(columnasMatriz):

        for filas in range(filasMatriz-cantDeNumerosEnSecuencia):

            x = 1
            while m5x5[filas][columnas] == ((m5x5[filas+x][columnas])-x):

                if x == 3:
            
                    posInicial.insert(0, [filas, columnas])
                    posFinal.insert(0, [filas+x, columnas])
                    break
                x+=1

    for columnas in range(columnasMatriz):

        for filas in range(filasMatriz-1, cantDeNumerosEnSecuencia-1, -1):

            x = 1
            while m5x5[filas][columnas] == ((m5x5[filas-x][columnas])-x):

                if x == 3:
            
                    posInicial.insert(0, [filas, columnas])
                    posFinal.insert(0, [filas-x, columnas])
                    break
                x+=1

def main():

    matriz5x5 = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 2, 4],
        [3, 5, 5, 4, 3],
        [4, 5, 2, 3, 2],
        [5, 4, 3, 2, 1]
    ]#R.random.randint(1, 6, size=(filasMatriz, columnasMatriz))

    scanHorizontal(matriz5x5)
    scanVertical(matriz5x5)

    for i in range(0, len(matriz5x5)):
        print(matriz5x5[i])
    
    print(posInicial)
    print(posFinal)

main()