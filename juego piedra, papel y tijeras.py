import random
from time import sleep

op = ["piedra", "papel", "tijeras"]
sep = "-" * 15

while True:
    user = input("Elige: piedra, papel o tijeras: ").lower()

    sleep(0.5)

    if user not in op:
        print("\nOpción no válido")
        continue

    pc = random.choice(op)

    sleep(0.5)
    
    print(f"\nPC: {pc}")

    if user == pc:
        print(f"\nEmpate, ambos eligieron {user}")

    elif user == "piedra" and pc == "tijeras":
        print(f"\nGanaste!, {user} gana contra {pc}")

    elif user == "tijeras" and pc == "papel":
        print(f"\nGanaste!, {user} gana contra {pc}")

    elif user == "papel" and pc == "piedra":
        print(f"\nGanaste!, {user} gana contra {pc}")

    else:
        print(f"\nPerdiste!, {user} pierde contra {pc}")

    sleep(0.5)

    print(f"{sep}Findel juego{sep}")
    
