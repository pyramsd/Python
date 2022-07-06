# factorial de un nuemro
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
print(factorial(10))

''' Otra forma:

def facto(n):
    if n<0:
        print("el factorial de un numero negativo no existe")
    elif n==0:
        print(1)
    else:
        fact = 1
        while n>1:
            fact *= n
            n -= 1
        print(fact)
facto(5)

'''

''' Otra forma:

import math
def fact(n):
    print(math.factorial(n))
fact(3)

'''
