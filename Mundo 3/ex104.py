#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python
#só que fazendo a validação para aceitar apenas valor numérico.Ex: n = leiaInt('Digite n')

def leiaInt(n):

    while True:

        if n.isnumeric():
            print(f'Você digitou o número {n}')
            break
        else:
            print('\033[31mDigite um número inteiro válido')
            n = input('\033[32mTente novamente: \033[m').strip()


leiaInt(input('Digite um número: ').strip())
    
    



