#Crie um programa que vai ler vários nomes e colocar em uma lista
#Depois disso, mostre:
#A) Quantos números foram digitados
#B)A lista de valores, ordenada de forma decrescente
#C)Se o valor 5 foi digitado e está ou não na lista
lista = []
n = ''
while True:
    lista.append(int(input("Insira um número: ")))
    n = input('Quer continuar? [Enter para continuar, caso contrario digite "N"]').upper().strip()
    if n == 'N':
        lista.sort(reverse=True)
        break
print(f'Foram digitados {len(lista)} números\nOs valores digitados do maior para o menor foram {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')