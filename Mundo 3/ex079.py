#Crie um programa onde o usuário possa digitar vário valores numéericos e cadastre-os em uma lista
#Caso o número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente

listanumerica = []

while True:
    x = int(input("Digite um número: "))
    if x not in listanumerica:
        listanumerica.append(x)

    y = input("Quer terminar? Digite S para terminar ou enter para continuar").strip().upper()
    if y == 'S':
        break

print(sorted(listanumerica))




