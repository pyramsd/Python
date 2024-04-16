'''
La idea básica es que a veces el cuerpo de las personas produce demasiada proteína determinada. 
Eso puede causar todo tipo de estragos.

Pero si se puede crear una molécula muy específica (llamada microARN),
se puede evitar que se produzca la proteína. Esta técnica se llama interferencia de ARN.

Los cuatro nucleótidos que se encuentran en el ADN son adenina (A), citosina (C), guanina (G) y timina (T).
Los cuatro nucleótidos que se encuentran en el ARN son adenina (A), citosina (C), guanina (G) y uracilo (U).
'''

def to_rna(dna_strand):
    rna_strand = ""
    for i in dna_strand:
        if i == "G":
            rna_strand += "C"
        elif i == "C":
            rna_strand += "G"
        elif i == "T":
            rna_strand += "A"
        elif i == "A":
            rna_strand += "U"
    return rna_strand

print(to_rna('ACGTGGTCTTAA'))