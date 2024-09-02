#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
#O programa será interrompido quando o número solicitado for negativo
cont = 0
ta = 0
while True:
    if cont == 0:
        ta = int(input("Insira um número para ver a tabuada: "))
        if ta <= 0:
            print("Bye Bye")
            break
        print("-"*20)
    cont += 1
    print(f"{ta} x {cont} = {ta*cont}")    
    if cont == 10:
        cont = 0
        print("-"*20)        