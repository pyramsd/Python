# Dado un numero, devolver su tabla de multiplicar completa
"""
def tablaDeMultiplicar(n):
    print("Tabla de multiplicar de", n)
    for i in range(0, 13):
        print(n,"x",i,"=",n*i)

tablaDeMultiplicar(n)
"""

try:
    def tablaDeMultiplicar(n):
        print(f"Tabla de multiplicar de {n}")
        for i in range(0, 13):
            print(f"{n} x {i} =",n*i)

    tablaDeMultiplicar(10)
except NameError and TypeError:
    print("No puedes llamar a una funcion vacia ni con un parametro tipo string, tiene que ser tipo entero")
