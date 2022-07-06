# Dada una palabra, buscarla en una frase y devolver cuantas veces aparece en ella.

def contador_palabra(texto, buscar):
    quitar = ",;:.\n!\"'"
    for caracter in quitar:
        texto = texto.replace(caracter, "")

    texto = texto.lower()
    palabras = texto.split()
    diccionario_frecuencias = {}

    for palabra in palabras:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra] += 1
        else:
            diccionario_frecuencias[palabra] = 1

    for palabra in diccionario_frecuencias:
        if palabra == buscar.lower():
            frecuencia = diccionario_frecuencias[palabra]
            print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia} vez/veces")

contador_palabra("sergio es genial y cool, si ese es sergio", "sergio")

'''
def Buscar(frase, buscar):
    repetidas = frase.lower().count(buscar.lower())
    print(f"Hay {repetidas} concidencia/s en la frase")

Buscar("Hola soy sergio y sergio es genial y cool", "sergio")
'''
