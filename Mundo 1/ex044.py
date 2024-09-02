#Faça um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento
#À Vista: 10% de desconto, á vista no cartão 5% de desconto, em até 2x no cartão preço normal, 3x ou mais no cartão 20% de juros
cv = "\033[31m"
st = "\033[m"
pp = float(input("Digite o preço do produto: R$"))
fp = input("Qual é a forma de pagamento do produto? a'V'ista ou 'D'ividido no cartão? ").upper()
if fp == "V":
    f = input("qual é a forma do pagamento? 'D'inheiro ou 'C'artão? ").upper()
    if f == "D":
        print("o preço do produto terá 10% de desconto, seu preço total será de: R${:.2f}".format(pp * 0.9))
    elif f == "C":
        print("o preço do produto terá 5% de desconto, seu preço total será de: R${:.2f}".format(pp * 0.95))
    else:
        print("{}opção inválida de pagamento{}".format(cv, st))
elif fp == "D":
    f = int(input("Em quantas vezes gostaria de dividir no cartão? "))
    if f == 2:
        print("O valor do produto não terá Juros, você vai pagar {:.2f}".format(pp))
    elif f >=3:
        pj = pp * 1.2
        print("{}Você pagará 20% de juros pelo produto, você pagará {} parcelas de R${:.2f}, o produto total custará R${:.2f}{}".format(cv, f, pj / f, pj, st))
    else:
        print("{}opção inválida de pagamento{}".format(cv, st))
else:
    print("{}opção inválida de pagamento{}".format(cv, st))