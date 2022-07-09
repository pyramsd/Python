def cuadradoHueco(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("* ", end="")
            else:
                print(" ", end=" ")
        print()
cuadradoHueco(10)

''' OTRA FORMA:

def cuadradoHueco(n):
    for i in range(n):
        for j in range(n):
            print("*" if(i==0 or i==n-1 or j==0 or j==n-1) else" ", end=" ")
        print()
cuadradoHueco(10)

'''
