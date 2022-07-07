def raizCuadrada(n):
    sqrt = n/2
    var_temp = 0
    while sqrt != var_temp:
        var_temp = sqrt
        sqrt = (n/var_temp + var_temp) / 2
    print(sqrt)
raizCuadrada(16)
