#desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
a = float(input("Primeira medida do triângulo: "))
b = float(input("Segunda medida do triângulo: "))
c = float(input("Terceira medida do triângulo: "))
if a + b > c and a + c > b and b + c > a:
    print("é possível formar um triângulo")
else:
    print("não é possível formar um triângulo")