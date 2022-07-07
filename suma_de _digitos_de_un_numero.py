num = int(input("ingrese número: "))

result = 0

while num > 0:
    digit = num % 10
    result = result + digit
    num = num//10

print("La suma de sus digitos es", result)

""" OTRA FORMA:

num = int(input("ingrese número: "))
result = 0
for n in str(num):
    result += int(n)
print("La suma de sus digitos es", result)

"""
