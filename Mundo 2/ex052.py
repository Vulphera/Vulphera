#Faça um programa que leia se um número inteiro é um número primo
x = int(input("Digite um número para descobrir se ele é primo: "))
nd = 0
for c in range(1, x+1):
    if x % c == 0:
        nd += 1
        print("\033[32m", end = ' ')
    else:
        print("\033[31m", end = ' ')
    print(c, end = ' ')
if nd <= 2:
    res = ("\033[32m")
else:
    res = ("\033[31mnão ")
print("\n\033[mO número {} {}é um número primo\033[m, ele é divisível por {} números".format(x, res, nd))