try:
    from PyDictionary import PyDictionary
except Exception as e:
    print(f"{e}")

def define_word(word):
    dictionary=PyDictionary()
    full_definition = dictionary.meaning(word)
    return full_definition
print(define_word("dissonance"))
