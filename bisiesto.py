age = int(input("Digite el año: "))

if (age % 4 == 0 and age % 100 != 0) or age % 400 == 0:
  print("El año SÍ es bisiesto")
else:
  print("El año No es bisiesto")
