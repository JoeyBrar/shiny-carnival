try:
    from PyDictionary import PyDictionary
except Exception as e:
    print(f"{e}")

def define_word(word):
    dictionary=PyDictionary()
    full_definition = dictionary.meaning(word)
    #return full_definition
    word_type = list(full_definition.keys())[0]
    print(word_type)
    lst_definitions = full_definition.get("Noun")
    for i in lst_definitions:
        print(i)
    return "COMMAND DONE"
