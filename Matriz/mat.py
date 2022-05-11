"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

#Python 3.9.6

import numpy as R

posFinal = []
posInicial = []

def scanHorizontal(m5x5):

    for i in range(0, len(m5x5)):

        for j in range(0, len(m5x5[i])-3):

            if (m5x5[i][j] == (m5x5[i][j+1]-1)) and (m5x5[i][j] == (m5x5[i][j+2]-2)) and (m5x5[i][j] == (m5x5[i][j+3]-3)):

                posFinal.insert(0, [i, j])
                posInicial.insert(0, [i, j+3])

def scanVertical(m5x5):

    for j in range(0, len(m5x5)):

        for i in range(0, len(m5x5[j])-3):

            if (m5x5[i][j] == (m5x5[i+1][j]-1)) and (m5x5[i][j] == (m5x5[i+2][j]-2)) and (m5x5[i][j] == (m5x5[i+3][j]-3)):

                posFinal.insert(0, [i, j])
                posInicial.insert(0, [i+3, j])

def main():

    matriz5x5 =[[1, 2, 3, 4, 1],
                [1, 2, 5, 4, 2],
                [2, 3, 4, 1, 3],
                [5, 4, 3, 4, 4],
                [1, 5, 3, 4, 5]]#R.random.randint(1, 5, size=(7, 5))

    scanHorizontal(matriz5x5)
    scanVertical(matriz5x5)

    for i in range(0, len(matriz5x5)):
        print(matriz5x5[i])
    print(posFinal)
    print(posInicial)

main()