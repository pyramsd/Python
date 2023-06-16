def lista_numbers(n):
    lista = [i + 1 for i in range(int((n ** 2 + n) / 2))]
    return lista


def floyd(n):
    k = 0
    aux = ''
    for i in range(n):
        for j in lista_numbers(n)[k:k + i + 1]:
            aux += str(j) + "  "
        print(aux)
        aux = ''
        k += i+1


floyd(5)