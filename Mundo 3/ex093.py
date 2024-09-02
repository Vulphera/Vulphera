#Crie um programa que gerencie o aroveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

Jogador = {}
total = 0
Jogador["nome"] = input('Nome do jogador: ')
Jogador["partidas"] = int(input(f'Quantas partidas o jogador {Jogador["nome"]} jogou? '))
for c in range (0, Jogador["partidas"]):
    Jogador[f"gol {c+1}"] = int(input(f'Quantos gols foram feitos na {c+1}° partida: '))
    total += Jogador[f"gol {c+1}"]
Jogador["totalgol"] = total

print(f' O {Jogador["nome"]} jogou o total de {Jogador["partidas"]} partidas')
for c in range (0, Jogador["partidas"]):
    print(f'foi marcado {Jogador[f"gol {c+1}"]} na {c+1}° partida')
print(f'Dando o total de {Jogador["totalgol"]} gols')

