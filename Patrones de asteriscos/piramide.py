def piramide(n):
    mitad = round(n-1)
    resultado = ""
    for i in range(n):
        if i < n:
            nivel = ""
            for columan in range((n*2)-1):
                if mitad - i <= columan and mitad + i >= columan:
                    nivel += "*"
                else:
                    nivel += " "
            resultado += nivel + "\n"
    print(resultado)
piramide(4)


""" Otra forma:

def triangulo(n):
    for i in range(n+1):
        spc = n - i # spacios
        print(" " * spc + "* " * i)
triangulo(4)

"""

