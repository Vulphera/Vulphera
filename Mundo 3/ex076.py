#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em formula tabular

lispreco = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

for produtos in range(0, len(lispreco)):
    if produtos % 2 == 0:
        print(f'{lispreco[produtos]:.<25}', end = '')
    else:
        print(f'R$:{(lispreco[produtos]):>6.2f}')