#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint

chute = []
x = int(input('quantos jogos serão jogados na mega sena?:'))

for jogos in range (0, x):
    ndn = 0
    chute.clear()

    while True:
        N = randint(0, 60)
        if N not in chute:
            chute.append(N)
            ndn += 1
            if ndn == 6:
                break

    print(sorted(chute))




