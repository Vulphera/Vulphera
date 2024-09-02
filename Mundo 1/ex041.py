#Faça um programa que leia o ano de nascimento de um atleta e o classifique conforme sua categoria de acordo com a idade:
#até 9 anos: Mirim, até 14:infantil, até 19:Junior, até 25: Senior, acima: Master
from datetime import date
y = date.today().year
a = int(input("Digite o ano de nascimento do atleta: "))
ida = y - a
print("O atleta tem {} anos, por isso ele se enquadrará na categoria:".format(ida))
if ida <= 9:
    print("Jûnior")
elif ida <=14:
    print("Mirim")
elif ida <=19:
    print("Junior")
elif ida <= 25:
    print("Sênior")
else:
    print("Master")