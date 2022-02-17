num_1 = int(input("Ingrese un número: "))
num_2 = num_1
while num_2 <= num_1:
    num_2 = int(input("Ingrese un número: "))

print("Los numeros pares son:")

for i in range(num_1+1, num_2):
    if i % 2 == 0:
        print(i)

if num_2 == num_1 + 1:
    print("Numeros no encontrados")
