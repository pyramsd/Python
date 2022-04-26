print("Método split()")
# split() divide un string en una lista de forma que cada palabra es un elemento de una lista

mensaje = "Hola mundo cruel"

print(mensaje, "->", mensaje.split())

print("----------------------------------------------")

print("Método strip()")
# .strip() elimina los spacios de inicio y fin

mensaje = "Hola"    
mensaje2 = "      mundo cruel" 

print("Sin el método strip() ->", mensaje, mensaje2)
print("Con el método strip() ->", mensaje, mensaje2.strip())

print("-----------------------------------------------")

print("Método replace()")

mensaje = "Elemento A"

print(mensaje, "->", mensaje.replace("A","B"))
                   # elemento a reemplazar(A), reemplazo(B)
