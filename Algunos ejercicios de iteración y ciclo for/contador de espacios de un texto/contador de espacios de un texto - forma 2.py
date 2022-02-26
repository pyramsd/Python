texto = input("Ingrese texto: ")

palabras = texto.split()

espacios = len(palabras) - 1

print("El texto tiene", len(palabras), "palabras. Por lo tanto tiene", espacios, "espacio/s")


