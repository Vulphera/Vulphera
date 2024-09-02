#Crie um código em Python que teste se o site Pudim está acessível pelo computador usado
import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está funcionando')
else:
    print('O site está funcionando com sucesso')






