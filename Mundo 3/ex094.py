#Crie um programa que leia nome, sexo, idade de várias pessoas, guardando os dadaos de cada pessoa em um dicionário e todos os dicionários em uma lista, no final mostre:
#A)Quantas pessoas cadastradas
#B)A média de idade
#C)Uma lista com mulheres
#D)Uma lista com idade acima da média

pessoa = {}
galera = []

while True:
    pessoa.clear()
    pessoa["nome"] = input("Nome:")
    while True:
        sexo = input("Sexo: [M]asculino/[F]eminino: ").strip().upper()[0]
        if sexo == 'M':
            sexo = 'Masculino'
            break
        elif sexo == 'F':
            sexo = 'Feminino'
            break
    pessoa["sexo"] = sexo
    pessoa["idade"] = int(input('Idade:'))
    galera.append(pessoa.copy())
    x = input('quer continuar? [Enter] para continuar/Digite [N]ão para finalizar: ').strip().upper()
    if x == 'N':
        break
   
print(galera)







