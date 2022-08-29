def decode(string):
    outstring           = ''
    counter             = ''
    for x in string:
        if x.isdigit():
            counter += x
        else:
            outstring += x * (int(counter) if counter != '' else 1)
            counter     = ''
    return outstring

def encode(string):
    outstring           = ''
    outlist             = []
    for x in string:
        if outlist == [] or (len(outlist[-1]) != 0 and outlist[-1][0] != x):
            outlist.append(x)
        else:
            outlist[-1] += x
    for x in outlist:
        if len(x) != 1:
            outstring += str(len(x))
        outstring += x[0]
    return outstring
print(encode("hooolaaaa"))
print(decode("h3ol4a"))
