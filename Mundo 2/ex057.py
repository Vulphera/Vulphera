#Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F', caso esteja errado peça a digitação novamente até ter um valor correto
x = input("Escolha o seu sexo: [M/F]").upper().strip()[0]
'''while x != "M" and x != "F":'''
while x not in ["M", "F"]:
    x = input("Tente novamente: [M/F]").upper().strip()[0]
print("Você escolheu: ", x)