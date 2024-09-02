#crie um programa que leia duas notas dos alunos e que faça a média 
#media abaixo de 5 = reprovado
#media entre 5 e 6.9 - recuperação
#média acima de 7 = aprovado
a = float(input("Digite a média do aluno: "))
b = float(input("Digite a outra média do aluno: "))
m = (a+b)/2
if m < 5:
    print("\033[31mReprovado\033[m")
elif m < 7 and m >=5:
    print("\033[33mRecuperação\033[m")
else:
    print("\033[32mAprovado\033[m")