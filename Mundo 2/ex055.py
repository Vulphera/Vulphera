#Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e qual foi o menor peso lido
we = 0
M = 0
m = 0
for c in range (0, 5):
    we = float(input("Digite o peso da {} pessoa: ".format(c+1)))
    if c == 0:
        m = we
        m = we
    elif we > M:
        M = we
    elif we < m:
        m = we

    if we > M:
        M = we
    elif we < m:
        m = we
print("A pessoa mais pesada pesa {}Kg, e a pessoa mais leve pesa {}Kg".format(M, m))