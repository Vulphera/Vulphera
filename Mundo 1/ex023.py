#faça um programa que leia do número 0 até 9999 e mostre cada um dos dígitos separados entre unidade dezena centena e milhar
ne = int(input("insira um número entre 0 a 9999: "))

U = ne // 1 % 10
D = ne // 10 % 10
C = ne // 100 % 10
M = ne // 1000 % 10
print("Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}".format(U, D, C, M))