#Refaça o desaafio 009 mostrando a tabuada de um número que o usuário escolher utifilando um laço "for"

x = int(input("Qual tabuada gostaria de ver? "))
print("_"*20)
for c in range(1, 11):
    t = x * c
    
    print("{}x{}={}".format(x, c, t))
print("_"*20)