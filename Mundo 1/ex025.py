#crie um programa que verifique se existe "Silva" no nome da pessoa
ts = input("digite seu nome completo: ").strip()
print("Esse nome tem silva? {}".format(ts.upper().find("SILVA") == "SILVA"))