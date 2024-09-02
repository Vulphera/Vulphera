#Faça um mini-sistema que utilize o interactive help do python.
#O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS:use cores

hue = ('\033[m', #0 --- Sem cores/Limpa formatação
       '\033[0;30;41m', #1 --- Vermelho
        '\033[0;30;42m', #2 --- Verde
        '\033[0;30;43m', #3 --- Amarelo
        '\033[0;30;44m', #4 --- Azul
        '\033[0;30;45m', #5 --- Roxo
       )


def helping(c, col=0):
    print(hue[col], c.upper())
    print(hue[4])
    help(c)
    print(hue[0])



while True:
    comando = input('Insira uma função ou biblioteca: ')
    if comando.upper() == 'FIM':
        print('Obrigado por usar Python help')
        break
    if comando == '':
        print('erro')
    else:
        helping(comando, 1)






