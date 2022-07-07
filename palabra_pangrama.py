# palabra o oracion que contenga todas las letras de la a hasta la z
def is_pangram(sentence):
    sentence = sentence.lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in sentence:
            return False
    return True
print(is_pangram("qwertyuiopasdfghjklzxcvbnm"))
print(is_pangram("wertyuisdfghjcvbn"))
