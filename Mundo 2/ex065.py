#crie um programa que leia vários números inteiros pelo teclado, no final da execução, mostra a média entre todos os valorers lidos
#o programa deve perguntar do usuário se ele quer ou não continuar a digitar valores

continuar = ''
media = 0
x = 0
y = 0
while continuar not in ("N", "Nao", "Não"):
    media += 1
    y = int(input("digite um número para tirar a média: "))
    x += y
    print(media)
    print(x)
    
    continuar = input("Quer continuar?\nPressione enter para continuar\nDigite N ou Não para parar: ").title().strip()
print("A média dos números somados é: {}".format(x / media))
    

