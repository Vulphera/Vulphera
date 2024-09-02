#faça um programa que leia 5 valores numéericos e guarde-os em uma lista
#no final mostre qual foi o maior ee qual foi o menor valor digitado e as suas respectivas posições na lista

lista = list()
for c in range(0, 5):
    lista.append(int(input('insira um valor numérico: ')))

for c, v in enumerate(lista):
    if v == sorted(lista)[0]:
        M = c
    if v == sorted(lista)[-1]:
        m = c

print(f'o menor valor da lista é : {sorted(lista)[0]} e foi o {M+1}° a ser digitado\nE o maior valor da lista é: {sorted(lista)[-1]} e foi o {m+1}°e a ser digitado')

