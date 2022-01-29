import random

num = random.randint(100,999)
print("El número inicial es:",num)

c3 = num % 10
c2 = int((num % 100) / 10)
c1 = int((num - (num % 100)) / 100)

num_invert = int(str(c3)+str(c2)+str(c1))
print("El número invertido es:",num_invert)

invertsum5 = num_invert + 5
print("El número invertido sumado más 5 es:", invertsum5)
