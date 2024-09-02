#Escreva um programa que leia o número n1 inteiro qualquer e mostre na tela os primeiros n2 elementos de uma sequencia de fibonatti


n1 = 1
n2 = int(input("Quantas vezes gostaria de fazer: "))
n3 = 0
n4 = 0
while n2 >= n3:
    n3 += 2
    print(n4, end = ' ')
    if n2 >= n3:
        print(n1, end = ' ')
    n4 += n1
    n1 += n4
