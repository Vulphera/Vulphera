#Crie um programa que tenha um função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
#retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições 


def voto(y):
    """_summary_
    
    Args:
        y (_int_): Ano de nascimento
    """    
    from datetime import date
    x = date.today().year - y
    print(f'Este ano você completou ou completará {x} anos, portanto',end=' ')
    if x < 16:
        return ',porém com menos de 16 anos o voto é NEGADO'
    elif x < 18 or x > 65:
        return 'o voto se torna OPCIONAL'
    else:
        return 'o voto se torna OBRIGATÓRIO'

print(voto(y = int(input('Digite o ano em que você nasceu: '))))



