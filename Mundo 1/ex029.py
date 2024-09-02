#escreva um programa que leia a velocidade de um carro e o multe por R$7.00 para cada 1km/h acima do limite
x = float(input("Digite a velocidade do carro em Km/h: "))
if x <= 80:
    print("está dentro do limite")
else:
    y = x - 80
    print("Você seráa multado em R${:.2f} ".format(y * 7))