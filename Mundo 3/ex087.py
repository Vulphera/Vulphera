#Aprimore o desafio anterior, mostrando no final:
#A)A soma de todos os valores pares digitados
#B)A soma de todos os valores da terceira coluna
#C)O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
n=0
s = 0
sc3 = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        n+=1
        matriz[linha][coluna] = int(input(f'digite o {n}° valor'))

for linha in range (0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end = '')
    print()

for linha in matriz:
    for coluna in linha:
        if coluna % 2 == 0:
            s += coluna

sc3 = 0
for linha in range(0,3):
    sc3 += matriz[linha][2]

Mvsl = 0
for coluna in range (0, 3):
    if Mvsl < matriz[1][coluna]:
        Mvsl = matriz[1][coluna]
        
        
        
print(f'''a soma de todos os números pares será: {s}
A soma dos itens da coluna 3 é : {sc3}
O maior valor da segunda linha é: {Mvsl}''')