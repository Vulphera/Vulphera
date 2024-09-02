#escreva um programa que leia dois números inteiros, compare-os, mostrando na tela a mensagem:
#se o primeiro valor é maior, ou o segundo, ou se são iguais
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
if n1 > n2:
    print("{} é maior que {}".format(n1, n2))
elif n2 > n1:
    print("{} é maior que {}".format(n2 ,n1))
else:
    print("\033[033mAmbos tem o mesmo valor\033[m")