#Faça um programa que leia uma frase e mostre quantas vezes aparece a letra "A", a posição que ela aparece pela primeira vez e a ultima vez
frase = input("Digite uma frase aqui: ").strip()
print("a letra A aparece em um total de: {} na frase {}".format(frase.upper().count("A"), frase))
print("a primeira letra A se encontra na posição {} e a ultima na posição {} na frase {}".format(frase.upper().find("A"), frase.upper().rfind("A"), frase))