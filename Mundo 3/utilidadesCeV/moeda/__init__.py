#Exercício 107

'''def aumentar(coin = 0, y = 0):

    """_summary_
    Aumenta x em y%

    Args:
        coin (_float_): _Valor para ser aumentado em porcentagem_
        y (_float_): _Quantos por cento será feito o acréscimo do número_
    
    """
    y = 1 + (y / 100) 
    coin *= y
    return coin

def diminuir(coin = 0, y = 0):
    """_summary_

    Args:
        coin (_float_): _Valor para ser diminuido em porcentagem_
        y (_float_): _Quantos por cento será feito o decréscimo do número_
    """    
    y = 1 - (y / 100)
    coin *= y 
    return coin

def dobro(coin = 0):
    coin *= 2
    return coin

def metade(coin = 0):
    coin /= 2
    return coin'''

#Exercício 108

def moeda(coin=0, moeda='R$:'):
    return f'{moeda}{coin:.2f}'.replace('.',',')

#Exercício 109

def aumentar(coin = 0, y = 0,format=False):

    """_summary_
    Aumenta x em y%

    Args:
        coin (_float_): _Valor para ser aumentado em porcentagem_
        y (_float_): _Quantos por cento será feito o acréscimo do número_
        format (bool, optional): _Função moeda será utilizada se for verdadeiro_. Defaults to False.
    
    """
    y = 1 + (y / 100) 
    coin *= y
    return coin if format == False else moeda(coin)

def diminuir(coin = 0, y = 0, format=False):
    """_summary_

    Args:
        coin (_float_): _Valor para ser diminuido em porcentagem_
        y (_float_): _Quantos por cento será feito o decréscimo do número_
        format (bool, optional): _Função moeda será utilizada se for verdadeiro_. Defaults to False.
    """    
    y = 1 - (y / 100)
    coin *= y 
    return coin if format == False else moeda(coin)

def dobro(coin = 0,format=False):
    """_summary_

    Args:
        coin (float): _Valor que será dobrado_. Defaults to 0.
        format (bool, optional): _Função moeda será utilizada se for verdadeiro_. Defaults to False.

    """    
    coin *= 2
    return coin if format == False else moeda(coin)

def metade(coin = 0, format=False):
    """_summary_

    Args:
        coin (float): _Valor que será dividido por 2_. Defaults to 0.
        format (bool, optional): _Função moeda será utilizada se for verdadeiro_. Defaults to False.

    """    
    coin /= 2
    return coin if format == False else moeda(coin)

def resumo(coin=0, aument = 0, reduz=0):
    print('_'*45)
    print('Análise de valores:'.center(45))
    print('_'*45)
    print(f'''Preço analisado: \t\t{coin}
{('_'*45)}
Preço aumentado em {aument}%: \t{aumentar(coin,aument ,True)}
Preço reduzido em: {reduz}%: \t{diminuir(coin,reduz,True)}
O Dobro do preço é: \t\t{dobro(coin,True)}
A metade do preço é: \t\t{metade(coin,True)}
{('_'*45)}
 '''.center(45))
