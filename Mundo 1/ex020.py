#Faça um programa que sorteie a ordem de 4 alunos
from random import shuffle
p1 = input("digite um nome: ")
p2 = input("digite um nome: ")
p3 = input("digite um nome: ")
p4 = input("digite um nome: ")
list = [p1, p2, p3, p4]
shuffle(list)
print("a ordem de apresentação será {}".format(list))
