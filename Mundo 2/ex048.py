#Faça um programma que calcule a soma de todos os número ímpares múltiplos de 3 no intervalo de 1 até 500
s = 0
hm = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        s += c
        hm += 1
print("A somatória dos {} valores entre 1 e 500, multiplos de 3 e ímpares é: \033[34m{}\033[m".format(hm, s))