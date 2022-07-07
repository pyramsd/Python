def palabrayPalabrainvert():
    palabra = input("ingrese una palabra: ")
    palabra = str(palabra)
    palabra_invert = palabra[::-1]
    count = 0

    """
    # variable[::-1] es una fórmula para invertir strings
    print(palabra_invert)
    """

    if palabra_invert == palabra:
        print("La palabra es palínformo")
    else:
        print("La palabra no es palíndromo")

count = 0

while count <= 3:
    count += 1
    palabrayPalabrainvert()
