# numero capicua

def capicua(n):
    n = str(n)
    if n[::-1] == n:
        print(f"{n} es Capicua")
    else:
        print(f"{n} NO es capicua")
capicua(2002)

