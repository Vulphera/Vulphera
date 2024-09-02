#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

Jogador = {}
team = []
golss = []


total = 0
while True:
    
    Jogador["nome"] = input('Nome do jogador: ').strip().title()
    Jogador["partida"] = int(input(f'Quantas partidas o jogador {Jogador["nome"]} jogou? '))
    for parti in range (0, Jogador["partida"]):
        gol = int(input(f'Quantos gols foram feitos na {parti+1}° partida: '))
        golss.append(gol)
        total += gol
    Jogador["gol"] = golss.copy()
    Jogador["totalgol"] = total
    total = 0
    team.append(Jogador.copy())
    Jogador.clear()
    golss.clear()
    if input('quer coninuar?: tecle N para parar ou enter para continuar').upper().strip() == 'N':
        break

print(f'''{'N°'}{'Nome':^30}{'Partidas':^16}{'Total de Gols':^32}
{'_'*100}''')

n = 0
for J in team:
    n += 1
    print(f'{n} {J["nome"]:^30}{J["partida"]:^16}{J["totalgol"]:^32}')
print('''


''')
while True:
    x = int(input("gostaria de ver os detalhes de algum jogador? digite o código do jogador ou 0 (zero) para encerrar: "))
    if x == 0:
        print('Obrigado por utilizar este programa')
        break
    else:
        while True:
            if x <= len(team):
                print("="*100)
                print(f'{'Nome':<30}{'Partidas':<20}{'Gols nas Partidas':>20}\n{'_'*100}')
                print(f'{team[x-1]["nome"]:<30}{team[x-1]["partida"]:^20}{", ".join(map(str, team[x-1]["gol"])):^18}')
                break
            else:
                print('este jogador não consta nos códigos acima, por favor, tente novamente')
                break
