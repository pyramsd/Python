n = int(input("Introduzca un número: "))
for i in range(n+1):
    spc = n - i # spacios
    print(" " * spc + "* " * i)
