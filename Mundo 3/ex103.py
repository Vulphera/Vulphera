#Faça um programa que tenha umaa função chamada ficha(), que receba dois parâmetros opcionais:
#O nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que um dado não tenha sido informado corretamente


def ficha(nome='<Desconhecido>', gols=0):
    """_summary_

    Args:
        nome (str): _Inserir nome do jogador_. Defaults to '<Desconhecido>'.
        gols (int): _inserir quantidade de gols feitos pelo jogador_. Defaults to 0.
    """    

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
        if nome=='':
            nome = '<Desconhecido>'
    print(f'O jogador {nome}, fez: {gols} gols')

nom = input('Nome do Jogador: ').strip().title()
gol = input('Gols feitos pelo jogador: ')
ficha(nom, gol)


