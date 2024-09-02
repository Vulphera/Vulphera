#Crie um programaa que tenha uma tupla com várias palavras (não usar acentos)
#Depois disso, você deve mostrar para cada palavra quais são suas vogais

palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'

for c in palavras:
    print(f'\nNa palavra {c} temos as vogais: ', end = '')
    for letra in sorted(c):
        if letra in 'aeiou':
            print(letra, end = ' ')
            