#Crie um programa que leia 2 valores e mostre um menu para soma, multiplicar, maior, novos numeros, sair do programa
select = 0
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo Valor: "))
while select != 5:
    print('''[1] Soma
[2] Multiplicação
[3] Qual é maior
[4] Digite outro valor
[5] Finalizar''')
    select = int(input("insira o comando: "))
    if select == 1:
        r = n1+n2
        print("A soma entre {} e {} é {}".format(n1, n2, r))
    elif select == 2:
        r = n1*n2
        print("A multiplicação entre {} e {} é {}".format(n1, n2, r))
    elif select == 3:
        if n1 > n2:
            print("{} é maior que {}".format(n1, n2))
        elif n2 > n1:
            print("{} é maior que {}".format(n2,n1))
        else:
            print("os valores são iguais")
    elif select == 4:
        print("informe os número novamente:")
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo Valor: "))
    elif select == 5:
        print("Goodbye")
    else:
        input("Operação inválida, tente novamente\ntecle enter para continuar ")
        
