# dado un array, devolver la cantidad de vocales y consonantes
vocales = ["a","e","i","o","u","á","é","í","ó","ú"]
consonantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

def numVocsnumCons(texto):
    texto = texto.lower()
    numVocs = []
    numCons = []
    texto=texto.lower()
    for i in texto:
        if i in vocales:
            numVocs.append(i)
        else:
            numCons.append(i)

    print(f"Consonantes: {len(numCons)}")
    print(f"Vocales: {len(numVocs)} ")

numVocsnumCons("Hola Chao")
