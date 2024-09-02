#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
#No Final mostre a matriz na tela com a formatação correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
n=0
for linha in range(0, 3):
    for coluna in range(0,3):
        n+=1
        matriz[linha][coluna] = int(input(f'digite o {n}° valor'))
for linha in range (0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end = '')
    print()
