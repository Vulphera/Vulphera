#Faça um programa que mostre a contagem regressiva de fogos de artifício indo de 10 até 0 com uma pausa de 1 segundo
from time import sleep
re = "\033[031m"
gr = "\033[32m"
st = "\033[m"
print("Contagem regressiva de fogos em:")
c ="0"
for c in range(10, -1, -1):
    if c > 3:
        print("{}{}".format(gr, c,))
    elif c < 4:
        print("{}{}".format(re, c,))
    sleep(1)
print("{}Feliz ano novo!{}".format(gr, st))