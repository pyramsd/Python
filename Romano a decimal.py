romano = input("Introduzca número romano: ")

def romano_a_decimal(romano):

    # Hacemos un diccionarios de los número romanos iniciales con su valor entera 
    romanos = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}
    
    # Creamos una variable inicial 0
    entero = 0

    # Con el ciclo for pasamos a cada uno de los indices que representa el número romano
    for i in range(len(romano)):
        
        # Si el iterable(i) es mayor a cero y si el valor que hay en 'romanos' que es la iteración de romano es mayor
        # que el valor de la iteración - 1
        if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]:
            # Al entero se le acumula  el valor de 'romano' - 2 por el valor de romanos - 1
            entero += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
            #Si no entonces solo acumulamos el valor de 'romanos'
        else:
            entero += romanos[romano[i]]
            
    print(entero)
    
romano_a_decimal(romano)
