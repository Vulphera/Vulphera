#Faça um programa que tenha um função chamada 'maior()', que receba vários parâmetros com valores inteiros
#Seu programa tem que analisar todos os valores e dizer qual deles é maior 
from time import sleep

def sep(S):
    for c in range(0,50):
        sleep(0.01)
        print(f"_",end = '', flush=True)
    print()
def maior(* n):
    M = c = 0
    sep(50)
    print(f'\nOs valores dados foram: ', end= '', )
    for x in n:
        print(f'{x}', end = ' ', flush=True)
        c += 1
        if x > M:
            M = x
        sleep(0.2)
    if c == 0:
        sleep(0.2)
        print(f'0', end='')
    sleep(0.2)
    print(f'\nForam analisados {c} valores e ', end='')
    sleep(0.2)
    print(f'o maior valor é {M}')
    sep(50)
    sleep(0.2)


maior(1, 3, 5, 7, 2, 4, 19)
maior()



