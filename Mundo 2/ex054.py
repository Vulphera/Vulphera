#Crie um proggrama que leia o ano de nascimento de 7 pessoas, no final mostre quantas pessoas não atingiram a maioridade e quantas são maiores
from datetime import date
y = date.today().year
x = 0
aa = 0
un = 0
for c in range(0, 7):
    x = int(input("Digite o ano do nascimento da {} pessoa: ".format(c+1)))
    z = y - x
    if z >= 18:
        aa += 1
    else:
        un += 1
print("Ao todo temos {} pessoas maiores de idade e {} pessoas menores de idade".format(aa, un))