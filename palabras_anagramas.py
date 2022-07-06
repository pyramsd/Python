# dado dos strings, identificar si son anagramas
def anagram_check(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if sorted(str1) == sorted(str2):
        print(f"{str1} y {str2} son anagramas")
    else:
        print(f"{str1} y {str2} no son anagramas")
anagram_check("Luis", "Suli")

""" Otra forma:

def anagram_check(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
print(anagram_check("ser","res"))

"""
