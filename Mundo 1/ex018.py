#Faça um programa que calcule o Seno, Cosseno e Tangennte
import math
degrees = float(input("digite um ângulo para se calculado: "))
print("o angulo de {} tem o seno de {:.2f}".format(degrees, math.sin(math.radians(degrees))))
print("o angulo de {} tem o cosseno de {:.2f}".format(degrees, math.cos(math.radians(degrees))))
print("o angulo de {} tem a tangente de {:.2f}".format(degrees, math.tan(math.radians(degrees))))
