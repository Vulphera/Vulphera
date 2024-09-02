#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema vai ter só 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from Library115 import menu
from time import sleep



if menu.verifica('texto_ex115b.txt'):
    print('arquivo encontrado')
else:
    print('O arquivo não existe\nCriando arquivo',end='',flush=True)
    for c in '...': #para efeito visual apenas
        sleep(0.5)
        print(c,end='',flush=True)
    print('')
    menu.criarquivo('texto_ex115b.txt')


while True:
    menu.titulo('Menu Principal')
    menu.options('Nome', 'Idade', 'Cadastro')
    try:
        opcao = menu.readint(Num = 'Gostaria de acessar qual cadastro?: ')
    except KeyboardInterrupt:
        print('Interrompido pelo usuário')
        break
    if opcao == 1:
        menu.titulo('Nome')
        menu.ler_arquivo('texto_ex115b.txt')
    elif opcao == 2:
        menu.titulo('Cadastro')
    elif opcao == 0:
        print('Saindo',end='',flush=True)
    
        for c in '...':
            sleep(0.5)
            print(c, end='', flush=True)
        sleep(0.5)
        print('')
        break
    else:
        print('Ocorreu um erro, aguarde...')


print('Programa Finalizado')


