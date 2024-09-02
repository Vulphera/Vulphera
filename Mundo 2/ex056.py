#Desenvolva um programa que leia o nome, Idade e sexo de 4 pessoas no final o programa mostre:
#A média da idade do grupo, qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos
import time
n = ""
a = 0
am = 0
Ma = 0
Mn = ''
Fa = 0
s = ""
for c in range(0, 4):
    print("_"*10, "{}° person's info".format(c+1),'_'*10)
    n = input("Insert this person's name: ").title()
    a = int(input("Insert this person's age: "))
    s = input("which sex are this person? [M]ale or [F]emale: ").strip().title()
    inicio = time.time()
    if s in ["F",  "Female"]:
        s = "Female"
    elif s == 'M' or s =="Male":
        s = "Male"
    else:
        s = "Unknown"
    if s == "Male":
        if a > Ma:
            Ma = a
            Mn = n
    if s == "Female":
        if a <= 20:
            Fa += 1
    am += a
print("O homem mais velho se chama {}, existem {} mulheres com 20 anos ou menos e a média da idade do grupo é: {:.0f}".format(Mn, Fa, am/4))
fim = time.time()
print(fim-inicio)