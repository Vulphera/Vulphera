#escreva um programa que pergunte a quantidade de km rodados e a quantidade de dias que um carro foi alugado, cobrando R$60.00 por dia e R$0.15 por km rodado
km = float(input("Km rodados "))
dias = float(input("dias queo carro estava alugado: "))
print("o total a ser pago será R$:{:.2f}".format(km * 0.15 + dias * 60))
