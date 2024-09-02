#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (Largura e comprimento) e mostre a área do terreno

def area(L, C):

    A = (L*C)
    print(f'a área deste local é de {A} M²')


x = float(input('Digite a largura do local em metros: '))
y= float(input('Digite o comprimento do local em metros: '))
area(x, y)



