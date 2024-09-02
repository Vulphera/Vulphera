#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostrte:
#A)Quantas vezes apareceu o valor 9
#B) em que posição foi digitado o valor 3 
#C) Quais foram os números pares
nupar = 0
numeros = (int(input('digite um número: ')),
    int(input('digite um número: ')),
    int(input('digite um número: ' )),
    int(input('digite um número: ')))

print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 foi digitado na posição {numeros.index(3)+1}')
print('os números pares digitados foram: ', end = ' ')
for n in numeros:
    if n % 2 == 0:
        nupar += 1
        print(n, end = ' ')
print(f'. Logo temos {nupar} números pares')

