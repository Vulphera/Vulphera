#Crie um progrma que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#no final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notasa de cada aluno individualmente

lista1 = []
lista2 = []

while True:
    lista2.clear

    N = input('Insira o nome do aluno(a): ')
    N1 = float(input('1° Nota: '))
    N2 = float(input('2° Nota: '))
    M = (N1 + N2) / 2
    lista2.append([N, [N1, N2], M])
    lista1.append(lista2[:])

    x = (input('quer continuar? enter para continuar ou digite [N] e enter para finalizar: ')).strip().upper()
    if x == 'N':
        break

for c, i in enumerate(lista1):
    print(f'''NO.{'Nome do aluno':<9}{'Média':>11} 
{c}) {i[c][0]:<13}{i[c][2]:>9.1f}''')
    
while True:
        x = int(input('gostaria de ter detalhes da nota de algum aluno?'))
        if x <= c:
            print(f'''{i[x][0]}
Nota 1:{i[x][1][0]}
Nota 2:{i[x][1][1]}''')
        elif x == 999:
            break
        else:
            print('tente de novo com o NO. do aluno')
        