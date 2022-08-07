def calculate(a, b):
    if b == 0: return 0
    elif b == 1: return a
    else: return a + calculate(a, b-1)

resultado = calculate(2, 5)
print(resultado)
