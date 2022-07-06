import math
print("Clcular área de un círculo")
radio = float(input("Intraduzca el valor del radio: "))
area = math.pi * (radio ** 2)

if radio < 1:
    print("El radio no puede ser 0 o menor que cero.")
elif radio >= 1:
    print(f"El área del círculo es {round(area, 2)}")
