#Faça um programa que leia um número qualquer e mostre seu fatorial com
f = 1
a = x = int(input("Digite um número para descobrir seu fatorial: "))
while x > 0:
    f *= x
    if x!= 1:
       print("{}x".format(x), end='')
    else:
        print("1=",end=' ')
    x -= 1
print("{} é o fatorial de {}!".format(f, a))