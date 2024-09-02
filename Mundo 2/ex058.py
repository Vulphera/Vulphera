#Melhore o jogo do exercício 28, só que até o jogador acertar o resultado, mostrando no final quantos palpites foram necessários
#ex:28 crie um programa que faça o computador escolher um numero entre 0 a 5, e o usuario deverá adivinhar o numero, e entao dizer se o usuario venceu ou perdeu
import random
x = random.randint(0, 10)
p = 1
t = int(input("Chute um numero entre 0 a 10: "))
while t != x:
    t = int(input("\033[31mtente novamente\033[m"))
    p += 1
if t == x:
    print("\033[32mParabéns você acertou\033[m, Você precisou de {} Palpites para chegar no número".format(p))
