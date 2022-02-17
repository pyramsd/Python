# Pedir un número y mostrar su tabla de multiplicar
number = int(input("Ingrese un número: "))
for i in range(1,13):
    print(number, "x", i, "=", (number*i))
