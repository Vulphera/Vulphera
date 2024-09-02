#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPaar()
#A primeira função vai sortear 5 números e vai colocálos dentro da lista 
#E a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anteiors
from time import sleep
from random import randint


lista = []

def sorteia():
    print('os seguintes números de 1 a 10 foram gerados: ', end='')
    for c in range(0, 5):
        x = randint(1, 10)
        print(f'{x}', end=' ',flush=True)
        lista.append(x)
        sleep(0.5)
    
def divpar():
    sopar = 0
    print()


    cont = 0
    for d in lista:
        if d % 2 == 0:
            cont += 1
    if cont == 1:
        print('O unico valor par nesta lista é:', end= ' ')
    elif cont == 0:
        print('não há valores pares nesta lista')
    else:
        print("Os valores pares da ultima lista são: ",end='')
    for d in lista:
        if d % 2 == 0:
            cont += 1
            sopar += d
            print(f'{d}', end= ' ', flush=True)
            sleep(0.5)
    print(f'e sua soma é igual a: {sopar}')


sorteia()
divpar()


