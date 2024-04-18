'''
Traducir secuencias de ARN en proteínas.
El ARN se puede dividir en tres secuencias de nucleótidos llamadas codones
y luego traducirse a un polipéptido así:

ARN: "AUGUUUUCU" => se traduce como Codones: "AUG", "UUU", "UCU" => que se convierten en un polipéptido
con la siguiente secuencia => Proteína: "Metionina", "Fenilalanina", "Serina"

Existen 64 codones que a su vez corresponden a 20 aminoácidos;

También hay tres codones de terminación (también conocidos como codones de 'PARADA');
si alguno de estos codones se encuentra (por el ribosoma), toda la traducción termina
y la proteína finaliza.

odos los codones posteriores se ignoran,
así: ARN: "AUGUUUUUUAAAAUG" =>
Codones: "AUG", "UUU", "UCU", "UAA", "AUG" =>
Proteína: "Metionina", "Fenilalanina", "Serina"

Tenga en cuenta que el codón de parada "UAA" finaliza
la traducción y la metionina final no se traduce a la secuencia de la proteína.
'''

dict = {
    'AUG':'Metionina',
    "UGG":"Triptofano",
    'AAA':'Lisina', 'AAG':'Lisina',
    'UAU':'Tirosina', 'UAC':'Tirosina',
    'UGU':'Cisteina', 'UGC':'Cisteina',
    'CAU':'Histidina', 'CAC':'Histidina',
    'CAA':'Glutamina', 'CAG':'Glutamina',
    'AAU':'Asparagina', 'ACC':'Asparagina',
    'UUU':'Fenilalanina', 'UUC':'Fenilalanina',
    'GAU':'Acido aspartico', 'GAC':'Acido aspartico',
    'GAA':'Acido glutammico', 'GAG':'Acido glutamico',
    'AUU':'Isoleucina', 'AUC':'Isoleucina', 'AUA':'Isoleucina',
    'GUU':'Valina', 'GUC':'Valina', 'GUA':'Valina', 'GUG':'Valina',
    'CCU':'Prolina', 'CCC':'Prolina', 'CCA':'Prolina', 'CCG':'Prolina',
    'GGU':'GLicina', 'GGC':'GLicina', 'GAA':'GLicina', 'GAG':'GLicina',
    'GCU':'Alanina', 'GCC':'Alanina', 'GCA':'Alanina', 'GCG':'Alanina',
    'ACU':'Treonina', 'ACC':'Treonina', 'ACA':'Treonina', 'ACG':'Treonina',
    'UUA':'Leucina', 'UUG':'Leucina', 'CUU':'Leucina', 'CUC':'Leucina', 'CUA':'Leucina', 'CUG':'Leucina',
    'CGU':'Arginina', 'CGC':'Arginina', 'CGA':'Arginina', 'CGG':'Arginina', 'AGA':'Arginina', 'AGG':'Arginina',
    'UCU':'Serina', 'UCC':'Serina', 'UCA':'Serina', 'UCG':'Serina', 'AGU':'Serina', 'AGC':'Serina',
    'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'}

def proteins(strand):
    protns = []
    for i in range(0, len(strand), 3):
        prot = dict.get(strand[i:i + 3])
        if prot == "STOP":
            break
        protns.append(prot)
    return protns

print(proteins('AUG'))
print(proteins('UUUUUU'))
print(proteins('UUAUUG'))
print(proteins('AUGUUUUGG'))
print(proteins('UGGUAG'))
print(proteins('AUGUUUUAA'))
print(proteins('UGGUAGUGG'))
print(proteins('UGGUGUUAUUAAUGGUUU'))
