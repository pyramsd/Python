def atbash(word):
    word = word.upper()
    cipher_word = ""
    for i in word:
        ascii = ord(i)
        if ascii >= 65 and ascii <= 90:
            position = ascii -65
            new_position = 25 -position
            new_ascii = new_position + 65
            new_letter = chr(new_ascii)
        else:
            new_letter = i
        cipher_word += new_letter
    return cipher_word.lower()

print(atbash("test"))
            # palabra
