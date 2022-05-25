palabra = input("Ingrese una palabra: ")
if palabra == palabra[::-1]: # variable[::-1] es una fórmula para invertir strings
    print(f"La palabra si es palindroma")
else:
    print("La palabra no es palindroma")
