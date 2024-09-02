#Melhore o exerecício 61 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos 
prt = int(input("Primeiro termo: "))
raz = int(input("Razão da PA: "))
x = prt + raz*9
y = prt
print(prt, end=' ')
count = 0
qt = int(input("Quantos termos quer mostrar?: "))
while count <= qt:
    count+=1
    print(prt,end='->')
    prt += raz
    if count == qt:
        qt = int(input("Pausa, quantos termos mais gostaria de ver?: "))
        if qt != 0:
            count = 0