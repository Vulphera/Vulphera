#refaça o exercício 35 e mostre qual tipo de triângulo será formado, Equilátero, Isóceles, Escaleno
a = float(input("Primeira medida do triângulo: "))
b = float(input("Segunda medida do triângulo: "))
c = float(input("Terceira medida do triângulo: "))
if a + b > c and a + c > b and b + c > a: 
    if a == b == c:
        print("\033[34mÉ possível montar um triângulo equilátero\033[m")
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("\033[34mÉ possível montar um triângulo retângulo\033[m")
    elif a == b or a == c or b == c:
        print("\033[34mÉ possível montar um triângulo isóceles\033[m")
    else:
        print("\033[34mÉ possível montar um triângulo escaleno\033[m")
else:
    print("\033[31mNão é possível formar um triângulo\033[m")
