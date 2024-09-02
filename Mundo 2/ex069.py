#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntara se o usuário quer ou não continuar. no final mostre:
#A) Quantas pessoas tem mais de 18 anos
#B) Quantos Homens foram cadastrados
#C) Quantas Mulheres tem menos de 20 anos
maisdezo = 0
M = 0
Wminustwenty = 0
while True:
    sex = input("Sexo da pessoa:\n[M]asculino\n[F]eminino\n").title().strip()[0]
    while sex not in ["M","F"]:
        sex = input("Digite uma das opções:\n[M]asculino\n[F]eminino\n").title().strip()[0]
    age = int(input("Digite a idade da pessoa: "))
    
    if sex == "M":
        M += 1
    if age >= 18:
        maisdezo += 1
    if age <=20 and sex == "F":
        Wminustwenty += 1

    cont = input("Quer continuar?: [S]im ou [N]ão: ").strip().upper()[0]
    while cont not in ["S","N"]:
        print("Tente novamente")
        cont = input("Quer continuar?: [S]im ou [N]ão: ").strip().upper()[0]
    if cont == "S":
            print("-"*20)
    else:
        break    
print(f"No grupo cadastrado temos {M} Homens, {Wminustwenty} Mulheres abaixo de 20 anos e {maisdezo} pessoas acima de 18 anos")