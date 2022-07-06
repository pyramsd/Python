# Dado un numero entero, inviertelo y devuelve de nuevo el entero.
def Invert_num(n):
    num = 0
    while n != 0:
        num = 10*num+n % 10
        n //= 10
    print(num)
Invert_num(67)

''' Otra forma:

def Num_Invert(n):
    n = str(n)
    print(n[::-1])
Num_Invert(67)

'''
