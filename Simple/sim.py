#Python 3.9.6

import random

#Variable para guardar el tamaño de la lista.
lenList = 10

#Función que crea la lista de diccionarios
def CreateDicList():

    #Creo la lista de {lenList} espacios vacíos
    dicList = [None] * lenList

    #Lleno la lista con diccionarios
    for i in range(0, lenList):

        dicList[i] = {'id':i+1, 'age': random.randint(1, 100)}

    return dicList

#Función que ordena la lista creada en {CreateDicList()}
def SortList(dicList):

    #Se guarda la lista desordenada en la variable que lo va a ordenar (Si bien no es necesario este pasamanos,
    #prefiero hacerlo para comparar las listas antes y después de los procesos).
    sortDicList = dicList
    ageList = [None] * lenList #Esta nueva lista guardará las edades a ordenar

    #Variable que guarda como se mostrará el id de la persona mas joven y mas vieja
    idMayMen = """
Id de la persona mayor: {}
Id de la persona menor: {}
"""

    for i in range(0, lenList): 

        ageList[i] = sortDicList[i]['age'] 

    ageList.sort(reverse=False)#Luego de guardar las edades en {ageList}, la ordeno de mayor a menor.

    # Las edades ordenadas en {ageList} se comparan con las de {sortDicList},
    # encontrando su posición para copiarlas e insertarlas al principio.
    # Luego se remueve la copia de su posicion final 
    for age in ageList:

        for i in range(0, lenList):

            if sortDicList[i]['age'] == age:

                x = 0
                sortDicList.insert(x, sortDicList[i])
                ++x
                sortDicList.pop(i+1)

    # Muestra el id de la persona mas vieja y joven
    print(idMayMen.format(sortDicList[0]['id'], sortDicList[9]['id']))
    return sortDicList

def main():

    # Muestra el id de la persona mas vieja y joven, seguido de la lista ordenada, al mandarle como parámetro la primera función.
    print(SortList(CreateDicList()))

main()