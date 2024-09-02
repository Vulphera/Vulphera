def leiadinheiro(mess=0):

    ok = False

    while not ok:
        mess = str(input('Insira um valor monetário: ').replace(',', '.')).strip()
        if mess.isalpha():
            print(f'\033[0;31m"{mess}" não é um valor inválido, tente novamente\033[m')
        elif mess == '':
            print(f'\033[0;31mPor favor, digite um valor válido\033[m')
        else:
            ok = True
            num = float(mess)
            return f'{num:.2f}'.replace('.',',')

