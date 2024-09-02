#escreva um programa para aprovar um empréstimo bancário para comprar uma casa
#o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal, savendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
vc = float(input("Digite o valor da casa: R$"))
sal = float(input("Digite o salário do comprador: R$"))
par = float(input("Em quantos anos será pago: ")) 
presm = vc / (par*12)
salpe = sal * 0.3
print("Para pagar uma casa de {} em {} anos a prestação mensal será de {:.2f}".format(vc, par, presm))
if salpe >= presm:
    print("\033[032mO empréstimo será aprovado\033[m")
else:
    print("\033[031mO empréstimo não será aprovado\033[m")
