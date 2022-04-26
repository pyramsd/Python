# concatenar
print("Concatenación:")

mensaje = "Hola"
espacio = " "
nombre = "Mario"
print(mensaje + espacio + nombre)

print("--------------------")
# no puedes concatenar un string con entero, antes tines que convertir a string al entero
numero = 5
str_numero = str(numero) # str -> convierte a string
print("El número es: " + str_numero)

print("---------------------")
# otra forma de concatenar es usando comas(,)
# la coma(,) asigna un espacio ya predefinido
print(4, 5) # puedes concatenar dos enteros
print(mensaje, espacio, nombre)
