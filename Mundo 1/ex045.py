#Crie um programa que faça o computador jogar Jo Ken Po com você 
from random import choice
from time import sleep
re = "\033[31m"
gr = "\033[32m"
ye = "\033[33m"
s = "\033[m"
print('''choose your next move:
[R]ock
[P]aper
[S]cisors''')
R = "Rock"
P = "Paper"
S = "Scisors"
p0 = input("I choose...").title().strip()
if p0 == "R" and "Rock":
    p = "Rock"
elif p0 == "P" and "Paper":
    p = "Paper"
elif p0 == "S" and "Scisors":
    p = "Scisors"
else:
    print("{}You didn't typed the right command{}".format(re, s))
    p = "Error"
lista = [R, P, S]
jkp = choice(lista)
if p != "Error":
    print("Jo")
    sleep(0.5)
    print("Ken")
    sleep(0.5)
    print("Po")
    sleep(0.5)
    print('''you Choose {}
the Computer Choose {}'''.format(p, jkp))
else:
    print("{}{}{}".format(re, p, s))
if p == "Scisors":
    if jkp == "Scisors":
        print("{}Draw{}".format(ye, s))
    elif jkp == "Rock":
        print("{}You Lost{}".format(re, s))
    else:
        print("{}You Won!{}".format(gr, s))
elif p == "Rock":
    if jkp == "Scisors":
        print("{}You Won!".format(gr, s))
    elif jkp == "Rock":
        print("{}Draw!{}".format(ye, s))
    else:
        print("{}You Lost{}".format(re, s))
elif p == "Paper":
    if jkp == "Scisors":
        print("{}You lost{}".format(re, s))
    elif jkp == "Rock":
        print("{}You Won!{}".format(gr, s))
    else:
        print("{}Draw{}".format(ye, s))
