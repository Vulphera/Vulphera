#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um numero de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade


def leiaInt():    
    while True:
        try:
            Inteiro = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mDigite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[32mInterrompido pelo usuário\033[m') 
            break
            #return 0
        else:
            return Inteiro
    
def leiaFloat():
    while True:
        try:
            n = input('Digite um número: ').replace(',', '.')
            Float = float(n)
        except (ValueError, TypeError):
            print('\033[31mDigite um número válido\033[m')
        except (KeyboardInterrupt):
            print('\033[32mInterrompido pelo usuário\033[m')
        else:
            return Float


num1 = (leiaInt())
num2 = (leiaFloat())

print(f'O número inteiro digitado foi {num1} e o número real digitado foi {str(num2).replace('.', ',')}')