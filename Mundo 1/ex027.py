#Faça um programaque leia o nome completo de uma pessoa e depois diga o primeiro e último nome dessa pessoa
nc = input("Digite seu nome completo: ").title().strip()
ncs = nc.split()
print("muito prazer, seu primeiro nome é {} e o último {}".format(ncs[0], ncs[len(ncs)-1]))
