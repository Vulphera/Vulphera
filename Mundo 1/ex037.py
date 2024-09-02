#Faça um programa que leia um número inteiro e escreva a base de conversão 
n = int(input("Insira um número inteiro para a conversão: "))
w = input("Gostaria de converter para 'B'inário, 'O'ctal ou 'H'exadecimal: ").upper()
if w == "B":
    print("{} em binário é: {}".format(n, bin(n)))
elif w == "O":
    print("{} em octal é: {}".format(n,oct(n)))
elif w == "H":
    print("{} em Hexadecimal é: {}".format(n, hex(n)))
else:
    print("\033[031mError, try again\033[m")
