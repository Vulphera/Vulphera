#faça um programa que leia algo e mostre seu tipo primitivo
x = input("Digite algo aqui: ")
print("o tipo primitivo desse valor é {} \n Só tem espaços? {} \n é um número? {} \n é alfabético? {} \n ".format(type(x), x.isspace(), x.isnumeric(), x.isalpha()))
print("é alfanumérico? {} \n tem letras Maiúsculas? {} \n tem letras minúsculas? {} \n Está capitalizada? {}".format(x.isalnum(), x.isupper(), x.islower(), x.istitle()))