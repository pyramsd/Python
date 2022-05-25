num = int(input("ingrese número: "))

result = 0

for n in str(num):
    result += int(n)
    
print("La suma de sus digitos es", result)
