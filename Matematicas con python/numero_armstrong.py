"""
El número armstrong es igual a la suma de digitos elevados a la potencia de su número de cifras

Ejemplo: 153 = 1^3 + 5^3 + 3^3 = 153
153 es número armstrong
"""

n = input("Número a verificar: ")

def num_armstrong(n):

    count = 0

    for i in range(len(n)):
        count = count + (int(n[i]) ** len(n))

    if count == int(n):
        print("Sí es armstrong")
    else:
        print("No es armstrong")

num_armstrong(n)
