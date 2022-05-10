#Python 3.9.6

import random

def main():

    listaDeDicc = [None] * 10

    for i in range(0, len(listaDeDicc)):

        listaDeDicc[i] = {'id':i+1, 'age': random.randint(1, 100)}

    return listaDeDicc
 
main()