print("""======================================================
* programa que determina si un número es par o impar *
======================================================""")

numero = int(input("Intruduzca un número entero: "))

if numero % 2 == 0:
    print("El número",numero, "es par")
elif numero % 2 == 1:
    print("El número", numero, "es impar")

# - En caso de ingresar un número tipo float, saldrá un error en el programa -
