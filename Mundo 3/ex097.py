#Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro
#e mostre uma mensagem com tamanho adaptável

def escreva(a):
    print(f'_' * len(a), '\n')
    print(a)
    print('_' * len(a))

a = input('escreve uma budega aqui: ')
escreva(a)

