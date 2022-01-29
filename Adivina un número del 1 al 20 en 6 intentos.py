import random

intentosRealizados = 0

print('Ingrese nombre, porfavor')

miNombre = input()

# 'random.randint()' función aleatoria de enteros
numero = random.randint(1, 20)

print('Hola ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:

    print('Intente adivinar.')
    estimacion = input(">> ")
    estimacion = int(estimacion)
    intentosRealizados = intentosRealizados + 1


    if estimacion < numero:

        print('Tu estimación es muy baja.')
    if estimacion > numero:
        print('Tu estimación es muy alta.')
    if estimacion == numero:

        # rompe el bucle while
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

if estimacion != numero:
    numero = str(numero)
    print('Pues no. El número que estaba pensando era ' + numero)
