#Faça um programa que sorteie um aluno entre quatro alunos
from random import choice
i1 = input("primeiro aluno: ")
i2 = input("segundo aluno: ")
i3 = input("terceiro aluno: ")
i4 = input("quarto aluno: ")
lista = [i1, i2, i3, i4]
print(choice(lista))
