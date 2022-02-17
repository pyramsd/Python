import random

numero1 = random.randint(1, 10)
numero2 = random.randint(1, 10)

print("¿Cuánto es " + str(numero1) + "+" + str(numero2) + "?")
respuesta = input("R = ")
if int(respuesta) == numero1 + numero2:
    print("CORRECTO")
else:
    print("NOP, la respuesta es " + str(numero1 + numero2))
