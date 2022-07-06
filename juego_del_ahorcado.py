import random

# Las constantes son variables que tienen por finalidad almacenar valores que nunca cambian desde la primera sentencia de asignación.
# imagen_ahorcado es una variable constante y mayormente se escriben con mayúsculas.
# La variable imagen_ahorcado es de valor lista, los valores lista empienzan con corchetes (línea 6) y terminan con corchetes (línea 62).
imagen_ahorcado = ["""

  +---+
  |   |
      |
      |
      |
      |
=========""", """

  +---+
  |   |
  0   |
      |
      |
      |
=========""", """

  +---+
  |   |
  0   |
  |   |
      |
      |
=========""", """

  +---+
  |   |
  0   |
 /|   |
      |
      |
=========""", """

  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========""", """

  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========""", """

  +---+
  |   |
  0   |
 /|\  |
 / \  | 
      |
=========""", """

  +---+
  |   |
 [0   |
 /|\  |
 / \  |
      |
=========""", """
  +---+
  |   |
 [0]  |
 /|\  |
 / \  |
      |
========="""]
palabras = "manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate pentagono hexagono heptagono octagono cuadrado triangulo rectangulo circulo elipse rombo trapezoide rojo naranja amarillo verde azul violeta blanco negro marron hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra".split()
# El (.split()) divide una cadena en una lista donde cada palabra es un
# elemento de la lista.

def obtenerPalabraAlAzar(listaDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(imagen_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(imagen_ahorcado[len(letrasIncorrectas)])
    print()

    print("letras incorrectas:", end= " ")

    # El operador (in) puede decir si un valor está en una lista o no. También funciona para las cadenas. Verifica si una
    #cadena existe en otra.
    for letra in letrasIncorrectas:
        print(letra, end= " ")
    print()

    espaciosVacios = "_" * len(palabraSecreta)

    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            # Los ":" indica corte en las listas.
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]

    for letra in espaciosVacios: # mostrar la palabra secreta con espacios entre cada letra    
        print(letra, end= " ")
    print()

def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        print("Adivina una letra.")
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print("Por favor, introduce una letra.")
        elif intento in letrasProbadas:
            print("Ya has probado esa letra. Elige otra.")
        elif intento not in "abcdefghijklmnñopqrstuvwxyz":
            print("Por favor ingresa una LETRA")
        else:
            return intento

def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print("¿Quieres jugar de nuevo? (sí o no)")
    return input().lower().startswith("s")
    # El (.startswith()) devuelve true si la cadena comienza con el valor especificado; de lo contrario false.

print("A H O R C A D O")
letrasIncorrectas = ""
letrasCorrectas = ""
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(imagen_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    # Permite al jugador escribir una letra
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print("¡Sí! ¡La palabra secreta es " + palabraSecreta + ". Has ganado!")
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento

        # Comprobar si el jugador ha agotado sus intentos y ha perdido
        if len(letrasIncorrectas) == len(imagen_ahorcado) - 1:
            mostrarTablero(imagen_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print("¡Te has quedado sin intentos!\nDéspues de " + str(len(letrasIncorrectas)) + " intentos fallidos y " + str(len(letrasCorrectas)) + " aciertos, la palabra era " + palabraSecreta)
            juegoTerminado = True

    # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ""
            letrasCorrectas = ""
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break
            
    









