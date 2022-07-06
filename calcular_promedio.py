# dado un array de numeros, devolver su promedio
def promedio(array):
    sum_elements = 0
    for i in array:
        sum_elements += i
    print(sum_elements/len(array))
promedio([2,3,4,5,56])

''' Otra forma:

def promedio(array):
    return sum(array)/len(array)
print(promedio([2,3,4,5,56]))

'''
