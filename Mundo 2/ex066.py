#crie um programa que leia varios números inteiros pelo teclado. O prograama só vai parar quando o usuário digitar o valor 999 que é a condição de parada
#No final mostre quantos números foram digitados e qual foi a soma entre eles
x = sum = 0
contador = 0
while True:
    x = int(input("Digite um número para fazer a soma, para parar digite 999: "))
    if x == 999:
        break
    sum += x
    contador += 1
print(f"O soma dos {contador} números é {sum}")