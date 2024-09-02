#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão contar apenas valores pares e os valores impares digitados respectivamente
#Ao final, mostre o conteúdo das três listas geradas
numeros = []
par = []
impar = []
while True:
    numeros.append(int(input('Insira um número: ')))
    con = input('enter para continuar ou digite N para finalizar a lista').upper().strip()
    if con == 'N':
        break
for x in numeros:
        if x % 2 == 0:
            par.append(x)
        elif x % 2 == 1:
            impar.append(x)
print(f'''os números pares digitados foram {par}
os números ímpares digitados foram {impar}
e o total de numeros digitados foram {numeros}''')


