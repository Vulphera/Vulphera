#Digite 3 valores e diga qual deles é o menor e qual deles é o maior
x = int(input("Digite um valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))
m = x
if y > z and y > x:
    m = y
if z > y and z > x:
    m = z
M = x
if y < x and y < z:
    M = y
if z < x and z < y:
    M = z
print(" o menor número é {} e o maior número é {}".format(M, m))