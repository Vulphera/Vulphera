#crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-so (com idade) em um dicionário
#se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import datetime

Dicio = {}

Dicio["nome"] = input('Insira seu nome: ')

dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year
dian = int(input('''data de nascimento: 
Dia: '''))
mesn = int(input('Mes: '))
anon = int(input('Ano: '))

if mesn > mes:
    idadeatual = ano - anon - 1
elif mes == mesn:
    if dia < dian:
        idadeatual = ano - anon - 1
else:
    idadeatual = ano - anon

Dicio["idade"] = idadeatual

Dicio["CTPS"] = int(input('Digite sua CTPS, caso não a tenha digite 0: '))
if Dicio["CTPS"] != 0:
    Dicio["contratação"] = int(input('Ano de contratação: '))
    Dicio["Salário"] = float(input('Salário: R$'))
    Dicio["aposentadoria"] = Dicio["idade"] + (Dicio["contratação"] + 35) - datetime.now().year
for k, v in Dicio.items():
    print(f'{k}: {v}')
