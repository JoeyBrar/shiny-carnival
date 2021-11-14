try:
    from PyDictionary import PyDictionary
except Exception as e:
    print(f"{e}")

def define_word(word):
    response=[]
    dictionary=PyDictionary()
    full_definition = dictionary.meaning(word)
    for index1, i1 in enumerate(full_definition):
        word_type = list(full_definition.keys())[index1]
        lst_definitions = full_definition.get(word_type)
        full_def=[]
        full_def.append(word_type)
        full_def+=lst_definitions
        response.append(full_def)
    return response
