print("====================")
print("= Menú de opciones =")
print("====================")

""" --------------------------------------------------- """

print("""1. Suma
2. Resta
3. Multiplicación
4. División
5. División entera
6. Potencia
7. Módulo o resto \n""")

""" --------------------------------------------------- """

num = int(input("Introduce la opción que deses: "))

if num == 1:
    print("Elegiste suma \n")
    num = int(input("Introduzca el primer valor: "))
    num += int(input("Introduzca el segundo valor: "))
    print("El resultado de la suma es:", num)
elif num == 2:
    print("Elegiste resta \n")
    num = int(input("Introduzca el primer valor: "))
    num -= int(input("Introduzca el segundo valor: "))
    print("El resultado de la resta es:", num)
elif num == 3:
    print("Elegiste Multiplicación \n")
    num = int(input("Introduzca el primer valor: "))
    num *= int(input("Introduzca el segundo valor: "))
    print("El resultado de la multiplicación es:", num)
elif num == 4:
    print("Elegiste división \n")
    num = float(input("Introduzca el primer valor: "))
    num /= float(input("Introduzca el segundo valor: "))
    print("El resultado de la división es:", round(num, 2))
elif num == 5:
    print("Elegiste división entera \n")
    num = int(input("Introduzca el primer valor: "))
    num //= int(input("Introduzca el segundo valor: "))
    print("El resultado de la división entera es:", num)
elif num == 6:
    print("Elegiste potencia \n")
    num = int(input("Introduzca el numero base: "))
    num **= int(input("Introduzca el numero exponente: "))
    print("El resultado del exponente es:", num)
elif num == 7:
    print("Elegiste módulo o resto \n")
    num = int(input("Introduzca el primer valor: "))
    num %= int(input("Introduzca el segundo valor: "))
    print("El resultado del módulo o resto es:", num)
else:
    print("Esa opción no existe")
