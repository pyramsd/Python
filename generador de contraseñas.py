import random

print("Contraseñas:")
print("""-Primero son las letras minúsculas
-Luego siguen números
-Luego siguen las letras mayúscula
-Y finalmente @ y # """)

class textos:
    
    # Objetos
    def __init__(self):
        self.caracteres = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        self.numeros = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.mayusculas = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "y", "Z")
        self.complementos = ("@", "#")

    # letras minus 
    def componer_texto(self,tam_texto):
        texto_final = ""
        for i in range(0,tam_texto):
            texto_final = texto_final + random.choice(self.caracteres)
        return texto_final

    # numeros
    def compon_numeros(self,tam_num):
        texto_nums = ""
        for j in range(0,tam_num):
            texto_nums = texto_nums + random.choice(self.numeros)
        return texto_nums

    # letras mayus
    def compon_mayus(self, tam_mayus):
        texto_mayus = ""
        for x in range(0, tam_mayus):
            texto_mayus = texto_mayus + random.choice(self.mayusculas)
        return texto_mayus

    # Complementos
    def compon_complementos(self, tam_complet):
        texto_complete = ""
        for y in range(0,tam_complet):
            texto_complete = texto_complete + random.choice(self.complementos)
        return texto_complete

mi_texto = textos()
for i in range(0,5):
    print(mi_texto.componer_texto(4) + mi_texto.compon_numeros(3) + mi_texto.compon_mayus(1)+ mi_texto.compon_complementos(2))
                         # modificable                  # modificable               # modificable                   # modificable                                    
