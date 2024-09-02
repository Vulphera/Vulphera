#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado
from random import randint
from operator import itemgetter

jogo = {}

jogo['Jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)

for k, v in jogo.items():
    print(f'O {k} tirou {v}')

lugar = sorted[jogo.items(), key = itemgetter(1), reverse=True]

for k1, v1 in enumerate(lugar):
    print(f'{k1+1} Lugar: {v1[0]} tirou: {v1[1]}')
