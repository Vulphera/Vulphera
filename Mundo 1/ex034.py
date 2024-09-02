#escreva um programa que pergunte o saalario e calcule o valor do aumento
#para salários superiores a R$1250.00, calcule aumento de 10%
#para salários inferiores ou iguais o aumento é de 15%
sal = float(input("Digite o valor de seu salário: R$"))
if sal > 1250:
    print("O aumento do seu salário de R${:.2f} vai para: R${:.2f}". format(sal, sal*1.1))
else:
    print("o aumento do seu salário de R$:{:.2f} vai para R{:.2f}".format(sal, sal*1.15))