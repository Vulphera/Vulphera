


def titulo(Título):
    print('-'*40)
    print(Título.center(40))
    print('-'*40)


def options(*args, saida = True):
    for number, itens in enumerate (args):
        print(f'{number+1} - {itens}')
    if saida:
        print('0 - Sair')

def readint(Num = ''):
    while True:
        try:
            Numero_Inteiro = int(input(Num))
        except ValueError:
            print('Por favor, digite um número')
        else:
            return Numero_Inteiro
        
import os

def diretorio(nome_arquivo):
    directory_now = os.getcwd()
    if os.path.basename(directory_now) == 'Curso em video':
        local_arquivo = os.path.join(directory_now, nome_arquivo)
    else:
        local_arquivo = os.path.join(directory_now, 'Curso em video', nome_arquivo)
    return local_arquivo

def verifica(nome_arquivo_verificar):

    local_arquivo_verificar = diretorio(nome_arquivo_verificar)
    
    print(f'Tentando abrir o arquivo em: {local_arquivo_verificar}')  # Debugging: imprime o caminho completo
    try:
        local_arquivo_verificar = open(local_arquivo_verificar, 'rt')
        local_arquivo_verificar.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarquivo(nome_arquivo_criar):

    try:
        local_arquivo = diretorio(nome_arquivo_criar)            
        with open(local_arquivo, 'wt+') as arq:
            pass
    except Exception as exc:
        print(f'\033[31mDesculpe, parece que o erro "{exc}" ocorreu\033[m')
    else:
        print(f'\033[32mO arquivo txt foi criado com sucesso em: {local_arquivo} com sucesso\033[m')


def ler_arquivo(nome_arquivo):
    local_arquivo = diretorio(nome_arquivo)
    try:
        arch = open(local_arquivo, 'rt')

    except:
        print('Um Erro inesperado ocorreu, por favor, tente novamente')
    else:
        print(arch.read())
    finally:
        arch.close()

def cadastrar(nome_arquivo, nome_cadastrado = '', idade_cadastrada = 0):
    local_arquivo = diretorio(nome_arquivo)
    try:
        arch = open(local_arquivo, 'at')
    except:
        print('erro')
    else:
        try:

            arch.write(f'Nome: {nome_cadastrado:<35} Idade: {idade_cadastrada}\n')
        except Exception as e:
            print(f'parece que o erro {e} ocorreu')
        else:
            print(f'O registro de {nome_arquivo} foi efetuado com sucesso')
    finally:
        arch.close()