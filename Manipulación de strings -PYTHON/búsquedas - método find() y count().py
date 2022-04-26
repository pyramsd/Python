# busqueda
print("Busquedas:")
print("Método find()")

mensaje = "Hola Juan"

find_subcadena = mensaje.find("R")
find_subcadena2 = mensaje.find("H")

# devuelve valores enteros

print(find_subcadena) # devolverá -1 al no encontrar el elemento en el string
print(find_subcadena2) # devolverá su posición(la primera posicion empieza desde 0)

print("-----------------------")
print("Método count()") # count() cantidad de una letra en especifica que hay el string

mensaje = "Hola Juan"

count_valor = mensaje.count("a") # cuantas "a"s hay
count_valor2 = mensaje.count("J") # cuantas "J"s hay

print(count_valor)
print(count_valor2)
