#crie um programa que leia varios números inteiros pelo teclado, o programa só vai parar quando o usuário digitar o valor 999, condição de parada
#No final mostra quantos números foram digitados e qual foi a soma desconsiderando a condição de parada
y = 0
x = 0
while y != 999:
    y = int(input("Digite um número inteiro, para parar digite 999: "))
    x += y
print("A soma de todos os números digitados é: {}".format(x-999))