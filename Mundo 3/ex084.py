#Faça um programa que leia o nome e peso de várias pessoas, guardaando tudo em uma lista. No final mostre:
#A)Quantas pessoas foram cadastradas 
#B)Uma listagem com as pessoas mais pesadas
#C)Uma listagem com as pessoas mais leves

info = []
total = []
pes = 0
M = m = 0
Ms = ms = ''
while True:
    info.append(input('Nome: '))
    info.append(int(input('Peso: ')))
    if info[1] > M:
        M = info[1]
        Ms = info[0]
    if len(total) == 0:
        m = info[1]
        ms = info[0]
    elif info[1] < m:
        m = info[1]
        ms = info[0]
    total.append(info[:])
    
    info.clear()
    x = input('Quer continuar? [S]im ou [N]ão: ').strip().upper()
    pes += 1
    if x == 'N':
        break

print(f'''Foram cadastradas {pes} pessoas
A pessoa mais pesada é: {Ms} pesando {M}
E a Pessoa mais leve é: {ms} pesando {m}''')