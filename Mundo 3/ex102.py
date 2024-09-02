#Crie um programa que tenha ua função fatorial() que receba dois parâmetros: 
#o primeiro que indique o NÚMERO a calcular e o outro chamado SHOW, que será um valor 
#lógico(opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial

def fatorial(x, show=False):
    """_Calcula o fatorial de um número_
Args:
x (_int_): __Número para realizar o fatorial__
show: __Se 'show = True' a conta do fatorial será apresentada__. Defaults to False.

Returns:
_int_: _Resultado do fatorial_
    """    

    f = 1
    for c in range(x , 0, -1):
        
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c

    return f


print(fatorial(5))
print(fatorial(5, show=True))
#help(fatorial)


