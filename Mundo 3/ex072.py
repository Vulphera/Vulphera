#Crie um programa que tenha uma tupla totaalmente preenchida com uma contagem por extenso, de 0 a 20
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mestrá-lo por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', ',onze', 'doze', 'treze',
    'quatorze', 'quinze', 'dezeseis', 'desessete', 'dezoito', 'dezenove', 'vinte')
search = int(input("Digite um número de 0 a 20 para tê-lo escrito por extenso: "))
while 0 > search or search > 20:
    search = int(input("Digite outro número dentro de 0 a 20: "))
    
print(f"O número digitado foi o número {numeros[search].title()}")