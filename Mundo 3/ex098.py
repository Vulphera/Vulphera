#Faça um programa que tenha um função chamada contador(), que receba três parâmetros: Inicio, Fim e passo.
#Seu programa tem que realizar três contagens atravês da função criada
from time import sleep

def contador (I, F, P):
    
    print(f'A contagem de {I} até {F} de {P} em {P} é: ', end= ' ',flush=True)
    if I <= F:

        while True:

            print(I, end = ' ', flush=True)
            sleep(0.5)
            I += P
            if I == F:
                print(I)
                break
            elif I >= F:
                break
    
    elif I >= F:

        while True:
                
            print(I, end = ' ', flush=True)
            sleep(0.5)
            I -= P
            if I == F:
                print(I)
                break
            elif I <= F:
                break

x = int(input('Inicio: '))

y = int(input('Fim: '))

z = int(input('De quantos em quanto números gostaria de fazer? '))


contador(x, y, z)
contador(y, x, z)




