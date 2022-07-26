# dado un numero, devolver sus divisores
def divisores(n):
    print(f"Los divisores de {n} son:")
    for i in range(n):
        i = i+1
        if n % i == 0:
            print(f"--> {i}")
divisores(6)
