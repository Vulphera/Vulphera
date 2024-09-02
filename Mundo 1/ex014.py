#faça um programa que possa calcular a conversão de graus Celsius e graus Fahrenheint
degree = input("type C to convert celsius to farenheit and F to convert farenheit to celsius:")
if degree == "C" :
  C = float(input("insert to convert Celsius to Farenheit: "))
  F = C * 9 / 5 + 32
  print(f"{F} degrees Farenheit")
elif degree == "F" :
  F = float(input("insert to convert Farenheit to Celsius: "))
  C = (F - 32) * 5 / 9
  print(f"{C} degrees Celsius")
else :
  print("error, check out for the right command")
input("Goodbye! ")
