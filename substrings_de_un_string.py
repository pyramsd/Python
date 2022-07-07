# dado un string, devolver todos sus substrings
def get_all_substrings(string):
    length = len(string)
    substrings = []
    for i in range(length):
        for j in range(i, length):
            substrings.append(string[i:j+1])

    print(substrings)
get_all_substrings("sergio")

''' Otra forma:

def get_all_substrings(string):
    res = [string[i: j] for i in range(len(string))
        for j in range(i + 1, len(string) + 1)]
    print(res)
get_all_substrings("abcde")

'''

''' Otra forma:

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

print(get_all_substrings('abcde'))

'''
