def triangulo(n):
    for i in range(n):
        for i in range(n-i):
            print("*", end=" ")
        print()
triangulo(5)
