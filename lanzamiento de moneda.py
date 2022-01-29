import random
print("Lanzaré una moneda 1000 veces. Adivina cuantas veces caerá cara. (Presiona enter para comenzar)")
input()
lanzamientos = 0
caras = 0
while lanzamientos < 1000:
    if random.randint(0, 1) ==1:
        caras = caras + 1
    lanzamientos = lanzamientos + 1

    if lanzamientos == 900:
        print("En 900 lanzamientos hubo " + str(caras) + " caras.")
    if lanzamientos == 100:
        print("En 100 lanzamientos, cara salió " + str(caras) + " veces")
    if lanzamientos == 500:
        print("De 500 lanzamientos cara salió " + str(caras) + " veces")

print()
print("De 1000 lanzamientos, al final cara salió " + str(caras) + " veces")
