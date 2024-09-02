#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separado os valores pares e impares
#No final , mostre os valores pares e ímpares em ordem crescente
 
nums = [[], []]

for c in range(0, 7):
    x = int(input('Digite um valor numérico: '))
    if x % 2 == 0:
        nums[0].append(x)
    else:
        nums[1].append(x)
nums[0].sort()
nums[1].sort()

print(f'Os números pares digitados fora {nums[0]} e os números ímpares foram {nums[1]}')
