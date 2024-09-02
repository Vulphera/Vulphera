#Faça um programa que possa calcular os Catetos e Hipotenusa
import math
catop = float(input("digite um numero para o cateto oposto: "))
catadj = float(input("digite um numero para o cateto adjacente: "))
print("hipotenusa cai medir {}".format(math.hypot(catop, catadj)))
