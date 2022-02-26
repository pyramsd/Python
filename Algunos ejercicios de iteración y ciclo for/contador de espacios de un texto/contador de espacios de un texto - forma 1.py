texto = input("Ingrese texto: ")

palabras  = texto.split()

# "i" es un contador
i = 0

while i < len(palabras):
    
    i += 1

espacios = len(palabras) - 1

print("Número de palabras es", i, "por lo tanto tiene", espacios, "espacios")
