def abbreviate(words):
    delete = "-_!,.'"
    acronym = ""
    for i in delete:
        if i == "'":
            words = words.replace(i, "")
        words = words.replace(i, " ")
    words = words.title()
    for i in words:
        if i.isupper():
            acronym += i
    print(acronym)
abbreviate("hola-ert")
