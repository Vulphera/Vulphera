#faça um programa que leia se um ano é ou não Bissexto
x = int(input("Digite um ano para ser analisado: "))
if x % 100 == 0 and x % 400 != 0:
    print("não é bissexto")
elif x % 4 == 0:
    print("é um ano bissexto")    
else:
    print("não é bissexto")     