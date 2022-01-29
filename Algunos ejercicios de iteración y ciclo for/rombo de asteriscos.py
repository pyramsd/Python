n = int(input("Introduzca número central: "))
def p(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("* " * (i +1))

    for j in range(n - 1, 0, -1):
        print(" " * (n -j), end="")
        print("* " * (j))
p(n)
