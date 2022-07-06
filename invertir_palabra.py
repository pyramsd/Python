# Dada una cadena de texto, darle La vuelta e invertir el orden de sus caracteres, sin usar
# métodos propios del Lenguaje, solo estructuras de control.
def Invert(texto):
    invert_string = ""
    for i in texto:
        invert_string = i + invert_string
    print(invert_string)
Invert("genial")

''' Otra de forma

def Invertir(text):
    text = text[::-1]
    print(text)
Invertir("Hola")

'''
