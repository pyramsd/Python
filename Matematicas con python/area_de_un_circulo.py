import math
print("Calcular area de un circulo")
radio = float(input("Intraduzca el valor del radio: "))
area = math.pi * (radio ** 2)

if radio < 1:
    print("El radio no puede ser 0 o menor que cero.")
elif radio >= 1:
    print(f"El area del circulo es {round(area, 2)}")
