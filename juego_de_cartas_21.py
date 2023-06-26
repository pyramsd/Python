import random

suma = 0

def get_random_number():
    num = random.randint(1, 13)
    return num

print("Juego de cartas 21\n")

while suma <= 21:
    num = get_random_number()
    seguirOSalirDelJuego = input("Pulse ENTER para pedir carta. Pulse 'q' para salir: ")
    print(f"El valor de la carta es {num}")

    if seguirOSalirDelJuego == "q": break
    else: suma += num

    print("La suma es {0}".format(suma))

if suma > 21: print(f"Perdiste - La suma total es {suma}")
else:
    num = get_random_number()
    print(f"La carta seleccionada del computador tiene el valor de: {num}")
    diferencia = suma - num
    if suma + diferencia <= 21: print(f"Pudiste Continuar. La suma seria {suma + num}")
    else: print("En buena hora")
