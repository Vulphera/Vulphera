#faça um programa que pergunte o ano de nascimento de um jovem e informe de acordo com sua idade:
#se ele ainda vai se alistar, se é a hora de ele se alistar ou se já passou da hora de ele se alistar
#o tempo deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
today = date.today().year
yg = int(input("Que ano ele nasceu?"))
age = today - yg
if age < 18:
    print("\033[32mAinda não é hora de se alistar, faltam {} anos\033[m".format(18 - age))
elif age == 18:
    print("\033[33mJá está na hora de se alistar\033[m")
else:
    print("\033[31mJá passou da hora de se alistar recruta, você está {} anos atrasado recruta!!\033[m".format(age - 18))