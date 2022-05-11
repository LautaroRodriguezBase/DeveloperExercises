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

    matriz = R.random.randint(1, 6, size=(filasMatriz, columnasMatriz))

    scanHorizontal(matriz)
    scanVertical(matriz)
    
    print("""
{}
    posiciones Iniciales: {}
    posiciones Finales:   {}
    """.format(matriz, posInicial, posFinal))

main()