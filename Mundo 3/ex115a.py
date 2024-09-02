#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vaia ter duas opções: cadastrar uma nova pessoa e listar as pessoas cadastradas

from Library115 import menu
from time import sleep





while True:
    resp = menu.opções('Sair', 'Nome', 'Idade', cab = 'Menu Principal')
    if resp == 1:
        print('\033[34m',end='')
        for c in 'Saindo...':
            print(c,end='',flush = True)
            sleep(0.2)
        print('\033[m')
        break
    elif resp == 2:
        menu.titulo('Nome')
    elif resp ==3:
        menu.titulo('Idade')
    else:
        print('\033[31m')
        for c in 'ERRO, por favor aguarde...':
            print(c,end='',flush=True)
            sleep(0.2)
        print('\033[m')





