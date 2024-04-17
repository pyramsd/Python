'''
Diferencia de hamming:

Tu cuerpo está formado por células que contienen ADN. Esas células se desgastan periódicamente
y necesitan ser reemplazadas, lo que logran dividiéndose en células hijas. De hecho,
¡el cuerpo humano promedio experimenta alrededor de 10 mil billones de divisiones celulares en su vida!

Cuando las células se dividen, su ADN también se replica. A veces, durante este proceso, se producen
errores y piezas individuales de ADN se codifican con información incorrecta. Si comparamos dos cadenas
de ADN y contamos las diferencias entre ellas podemos ver cuántos errores se produjeron. Esto se conoce
como la "Distancia de Hamming".

La distancia de Hamming solo se define para secuencias de igual longitud, por lo que intentar calcularla
entre secuencias de diferentes longitudes no debería funcionar.
'''

def distance(strand_a, strand_b):
    df = []
    if len(strand_a) != len(strand_b):
        raise ValueError("Las cadenas deben ser de igual valor.")
    count = 0
    for i, j in zip(strand_a, strand_b):
        if i != j:
            count += 1
            df.append((i, j))
    return f'Estas su distancia de hamming: {count}', f'Estas son sus diferencias {df}'

print(distance('GGACTGAAATCTG', 'GGACTGAAATCTG'))
print(distance('AGGACGGATTCT', 'GGACGGATTCTG'))
