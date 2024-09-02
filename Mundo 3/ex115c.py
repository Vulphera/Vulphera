from Library115 import menu
from time import sleep



if menu.verifica('texto_ex115c.txt'):
    print('arquivo encontrado')
else:
    print('O arquivo não existe\nCriando arquivo',end='',flush=True)
    for c in '...': #para efeito visual apenas
        sleep(0.5)
        print(c,end='',flush=True)
    print('')
    menu.criarquivo('texto_ex115c.txt')


while True:
    menu.titulo('Menu Principal')
    menu.options('Lista de cadastro', 'Cadastrar')
    try:
        opcao = menu.readint(Num = 'Gostaria de acessar qual opção?: ')
    except KeyboardInterrupt:
        print('Interrompido pelo usuário')
        break
    if opcao == 1:
        menu.titulo('Lista de Cadastro')
        menu.ler_arquivo('texto_ex115c.txt')
    elif opcao == 2:
        menu.titulo('Cadastrar')
        nome = input('Nome: ').strip()
        idade = menu.readint('Idade: ')
        menu.cadastrar('texto_ex115c.txt',nome, idade)
    elif opcao == 0:
        print('Saindo',end='',flush=True)
    
        for c in '...':
            sleep(0.5)
            print(c, end='', flush=True)
        sleep(0.5)
        print('')
        break
    else:
        print('deu ruim')


print('Programa Finalizado')


