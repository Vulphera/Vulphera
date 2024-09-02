#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final mostre os 10 primeiros termos dessa progressão
p = int(input("Primeiro termo da PA: "))
r = int(input("Razão da PA: "))
x = p + r*9
print("Dado o termo {} a razão de {} em uma PA será de: ".format(p, r))
for c in range (p, x+1, r):
    print(c)
    