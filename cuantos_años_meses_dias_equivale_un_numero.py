# dado un numero, mostrar a cuantos años, meses, dias equivale
def calcAMD(dias):
    años = dias//365
    dias_restantes = dias%365
    meses = dias_restantes//30
    dias_restantes = dias_restantes%30
    print(f"{dias} equivale a {años} años, {meses} meses y {dias_restantes} dias")
calcAMD(1095)
