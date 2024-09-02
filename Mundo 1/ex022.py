#crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiusculas, minusculas, quantas letras tem ao todo sem espaços 
#quantas letras tem no primeiro nome
nc = input("Digite seu nome completo: ")
print(nc.upper())
print(nc.lower())
ncse = nc.split( )
print(len("".join(ncse)))
print(len(ncse[0]))