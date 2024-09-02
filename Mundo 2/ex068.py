#Faça um programma que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
from random import randint
pcplay = 0
playerplay = 0
victories = 0
valor = 0
print("Vamos jogar par ou ímpar")
while True: 
    poui = (input("Quer par ou ímpar?\n[I]mpar\n[P]ar\n")).upper().strip()[0]

    pcplay = randint(1, 10)
    playerplay = int(input("Sua jogada"))
    valor = (pcplay + playerplay)%2

    print(f"você escolheu {poui} e jogou o número {playerplay} e o computadaor jogou {pcplay}")
    
    if valor == 1 and poui == "I" or valor == 0 and poui == "P":
        print("\033[32mVocê ganhou\033[m, continue jogando")
        victories += 1 
    else:
        break

print(valor)
print (f"\033[31mVocê Perdeu\033[m, mas você ganhou \033[33m{victories} vezes\033[m contra o computador")
