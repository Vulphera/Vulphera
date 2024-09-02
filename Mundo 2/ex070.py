#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. no final mostre:
#A)Qual é o gasto total da compra
#B)Quantos produtos custam mais de R$:1000.00
#C)Qual é o nome do produto mais barato

lowpname = ""
lowprice = 0
totalhighprice = 0
soma = 0

while True:
    x = ''
    pname = input("Digite o nome do produto: ")
    price = int(input("Digite o valor do produto: R$"))
    
    if lowprice == 0:
        lowprice = price
        lowpname = pname
    if lowprice > price:
        lowprice = price
        lowpname = pname

    if price >= 1000:
        totalhighprice += 1
        
    soma += price
    
    while x not in ["S","N"]:
        x = input("Gostaria de continuar?\n[S]im\n[N]ão\n").upper().strip()[0]
    if x == "S":
        print("-"*20)
    else:
        break
    
print(f"o produto mais barato é {lowpname}, você possui {totalhighprice} acima de R$:1000.00, e a soma total de todos os produtos é R${soma:.2f}")