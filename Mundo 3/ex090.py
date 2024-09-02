#Faça um programa que leia nome e média de um aluno, guardandao também a situação em um dicionário.
#no final, mostre o conteúdo da estrutura na tela

Dicio = {}
Dicio["nome"] = input("Nome do aluno: ")
nota = float(input('Média do aluno: '))
Dicio["media"] = nota
if nota >= 7 :
    Situation = 'aprovado'
else:
    Situation = 'reprovado'
Dicio["situação"] = Situation

print(f'Aluno: {Dicio["nome"]}\nMédia: {Dicio["media"]}\nSituação: {Dicio["situação"]}')
