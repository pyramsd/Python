import random

def dado():
    numero = int()
    numero = random.randint(1, 6)
    print("número generado >>", numero)
    print("¿Otro número? para otro número(s) y para cerrar programa(n)")
dado()

respuesta = input().lower()

while respuesta == "s":
    dado()
    respuesta = input().lower()
    if respuesta == "n":
        print("Programa cerrado")
