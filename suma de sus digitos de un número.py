num = int(input("ingrese número: "))

result = 0

while num > 0:
    digit = num % 10
    result = result + digit
    num = num//10

print("La suma de sus digitos es", result)
