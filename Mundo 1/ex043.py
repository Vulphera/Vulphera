#Faça um programa que calcule o IMC e mostre o status segundo a tabela abaixo:
#abaixo de 18.5: abaixo do peso, 18.5~25: peso ideal, 25~30: sobrepeso, 30~40:obesidade, acima de 40: obesidade mórbida
p = float(input("Digite aqui o seu peso em Kilogramas: "))
a = float(input("Digite aqui sua altura em Metros: "))
imc = p / (a ** 2)
print("Seu iMC é {:.2f}, Você apresenta".format(imc))
if imc < 18.5:
    print("\033[33mEstar abaixo do peso\033[m")
elif 25 > imc >= 18.5:
    print("\033[34m Peso ideal, Parabéns\033[m")
elif 25 <= imc < 30:
    print("\033[33mSobrepeso\033[m")
elif 30 <= imc < 40:
    print("\033[31mObesidadade, Tente se cuidar mais!\033[m")
else:
    print("\033[7mObesidade Mórbida, Cuidado!!]\033[m")