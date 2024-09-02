#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

parenteses = []
expressão = input('digite sua expressão: ')
for confere in expressão:
    if '(' in confere:
        parenteses.append('(')
    elif ')' in expressão:
        parenteses.pop()
if len(parenteses) == 0:
    print('não há nenhum erro')
else:
    print('Confira novamente sua expressão, algum parênteses está errado')
