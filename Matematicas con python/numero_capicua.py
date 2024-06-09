"""
Numero capicua: El número es capícua cuando se lee igual del derecho y al revés
"""

def es_capicua(num):
    num_original = num
    num_invertido = 0
    
    while num > 0:
        digito = num % 10
        num_invertido = num_invertido * 10 + digito
        num //= 10
    
    return num_original == num_invertido

numero = 12321
if es_capicua(numero):
    print(f"{numero} es un número capicúa")
else:
    print(f"{numero} no es un número capicúa")


""" Otra forma
def capicua(n):
    n = str(n)
    if n[::-1] == n:
        print(f"{n} es Capicua")
    else:
        print(f"{n} NO es capicua")
capicua(2002)
"""
