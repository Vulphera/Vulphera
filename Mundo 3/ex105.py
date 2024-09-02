#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
#A maior nota
#A média da turma
#A situação
#adicione também as docstrings

def notas(*n, situation = False):
    dicio={}
    dicio['Total de notas'] = len(n)
    dicio['Maior Nota'] = max(n)
    dicio['Menor Nota'] = min(n)
    dicio['Média'] = sum(n)/len(n)
    if situation:
        print('A situação da sala é ',end='')
        if dicio['Média'] >5:
            print('Ruim')
        elif dicio['Média'] >7:
            print('Razoável')
        else:
            print('Excelente')

    return dicio

print(notas(1, 3, 5, 7, 8, situation=True))
