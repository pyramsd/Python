filas = int(input("Número de columnas: "))
columnas = int(input("Número de filas: "))
for i in range(1, columnas+1):
    for j in range(1, filas+1):
        print("* ", end="")
    print(" ")
