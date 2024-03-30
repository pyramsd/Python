def isbn10(isbn : str):
    isbn = isbn.replace("-", "").replace(" ", "")
    canti = len(isbn)
    sum_pon = 0

    for i in isbn[:-1]:
        i = int(i)
        r = i * canti
        canti -= 1
        sum_pon += r

    r_final = sum_pon + int(isbn[-1])

    if r_final % 11 == 0:
        return True
    return False


print(isbn10("158-71 43-739"))
print(isbn10('0451524934'))


def validar_ISBN_13(isbn):
    isbn = isbn.replace('-', '').replace(' ', '')

    if len(isbn) != 13:
        return False

    if not isbn.isdigit():
        return False

    # suma_ponderada = sum(int(digito) * (1 if i % 2 == 0 else 3) for i, digito in enumerate(isbn))
    suma_ponderada = 0
    for i, digito in enumerate(isbn):
        if i % 2 == 0:
            suma_ponderada += int(digito)
        else:
            suma_ponderada += int(digito) * 3

    if suma_ponderada % 10 == 0:
        return True
    else:
        return False


print(validar_ISBN_13('978-612-4272-33-2'))
print(validar_ISBN_13('978-980-7716-26-0'))