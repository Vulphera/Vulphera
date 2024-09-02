##crie um programa que faça o computador escolher um numero entre 0 a 5, e o usuario deverá adivinhar o numero, e entao dizer se o usuario venceu ou perdeu
import random
x = random.randint(0, 5)
t = int(input("Chute um numero entre 0 a 5: "))
if t == x:
    print("Parabéns você acertou")
else:
    print("Você errou, tente novamente")