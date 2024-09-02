#Crie um programa que leia uma frase qualquer e diga se ela é ou não um palíndromo desconsiderando os espaços
pa = str(input("Digite uma palavra para ver se ela é um palíndromo: ")).strip().upper().split()
fusion = ''.join(pa)
invert = ""
invert = fusion[::-1]
result = ""
#for lt in range(len(fusion)-1, -1, -1):
#    invert += fusion[lt]

if fusion == invert:
    result == "\033[32m"
    print("é Um palindromo")
else:
    result == "\033[32mnão"
    print("não é um palindromo")

print("{} é {} ao contrário, logo {}é um palíndromo".format(fusion, invert, result))
