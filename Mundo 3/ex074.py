#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na Tupla.
from random import randint
listaaleatória = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(listaaleatória)
print(f'Dos números aleatórios gerados aleatoriamente de 0 a 10 teremos eles em sequência: {sorted(listaaleatória)}')
print(f'o menor número gerado aleatóriamente é o {sorted(listaaleatória)[0]}')
print(f'e o maior número é o {sorted(listaaleatória)[-1]}')