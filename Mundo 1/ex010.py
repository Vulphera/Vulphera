#010 Crie um conversor de quantos dólares poderá comprar com quantos reais tiver na carteira (cotação do dia 4.86)
rs = float(input("quantos reais tem na carteira? "))
print("você pode comprar {:.2f} dólares, mas adicionando as taxas de 5% do câmbio será: {:.2f}".format(rs/4.86, rs/4.86*0.95))