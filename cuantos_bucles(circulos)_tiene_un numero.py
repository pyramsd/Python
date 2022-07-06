# dado un numero, devolver cuantos bucles tiene el numero
# numeros con bucles: 0, 6, 8, 9 (numero que tienen circulos)
def bucles(n):
    nums_bucles = {0:1, 6:1, 8:2, 9:1}
    nums = []
    contador = 0
    n = str(n)
    for i in n:
        i = int(i)
        nums.append(i)
    for j in nums:
        if j in nums_bucles.keys():
            contador += nums_bucles[j]
    print(f"El numero {n} tiene {contador} bucle/s")
bucles(1288836)
