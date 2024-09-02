#desenvolva um programa que a distância de uma viagem em Km, cobraando R$0.50 por KM para viagens de até 200Km e R$0.45 para viagens mais longas
ddv = float(input("Digita a distância percorrida pelo passageiro: "))
if ddv <= 200:
    print("o preço da passagem será de R${:.2f}".format(ddv*0.5))
else:
    print("o preço da passagem será de R${:.2f}".format(ddv*0.45))