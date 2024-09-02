#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol na ordem de colocação. depois mostre:
#A) Os 5 primeiros
#B) Os últimos colocados
#C) Times em ordem alfabética
#D) Em que posição está o time Chapecoense (Já que ele não está na lista usaremos o Bragantino como exemplo)
Times = ("Palmeiras", "Grêmio", "Atlético", "Flamengo", "Botafogo", "Bragantino", "Fluminense", "Athletico-PR", "Internacional", "Fortaleza", "São Paulo", "Cuiabá",
    "Corinthians", "Cruzeiro", "Vasco", "Bahia", "Santos", "Goiás", "Coritiba", "América-MG")
print(f'os 5 primeiros times são: {Times[:5]}')
print(f'os últimos 4 times são {Times[-4:]}')
print(f'Os 20 times que apareceram em ordem alfabética são: {sorted(Times)}')
print(f'O time Bragantino está na {Times.index("Bragantino")} posição')
