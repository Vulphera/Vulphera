# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
ndc = input("Digite o nome de uma cidade: ").strip()
print(ndc[:5].upper() == "SANTO")