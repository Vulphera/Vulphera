#Faça um programa que simule o funcionamento de um caixa eletrônico.
 #No inicio pergunte ao usuário o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor ser]ao entregues
valorsacado = int(input("Digite o valor a ser sacado: R$"))
total = valorsacado
bn = 50
bntotal = 0
while True:
    if total >= bn:
        total -= bn
        bntotal += 1
    else:
        if bntotal > 0:
            print(f"{bntotal} Notas de {bn}")
        bntotal = 0
        if bn == 50:
            bn = 20
        elif bn == 20:
         bn = 10
        elif bn == 10:
            bn = 1
        if bn == 0:
            break