#Desenvolva um program que leia seis números inteiros e mostre a somaa apenas dos números pares, se o valaor for immpar desconsidere
s = 0
cn = 0
for c in range(0, 6):
    x = int(input("Digite 6 números: "))
    if x % 2 == 0:
        s += x
        cn += 1
print("A soma de todos os {} números pares é {}".format(cn, s))