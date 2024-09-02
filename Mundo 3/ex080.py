#Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista
#Já na posição correta da inserção sem usar o sort()
#no final mostre a lista ordenada na tela

ListaN = []
for c in range (0, 5):
    x = int(input("Digite um número: "))
    if c == 0 or x > ListaN[len(ListaN)-1]:
        ListaN.append(x)

    else:      
        where = 0  
        while True:            
            if x > ListaN[where]:
                where += 1
            else:
                ListaN.insert(where, x)
                break        

print(ListaN)



