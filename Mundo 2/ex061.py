#Refaça o exercício 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos de uma progressão usando while
#ex051:Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final mostre os 10 primeiros termos dessa progressão

prt = int(input("primeiro termo"))
raz = int(input("Razão da PA"))
x = prt + raz*9
y = prt
print(prt, end=' ')
while y < x:
    y += raz
    print(y,end=' ')

#Aproveitando e usando contagem
count = 1
while count <= 10:
    count+=1
    print(prt,end='->')
    prt += raz