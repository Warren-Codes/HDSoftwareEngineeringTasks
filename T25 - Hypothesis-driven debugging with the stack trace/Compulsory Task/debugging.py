
def print_values_of(dictionary):      # removed the second argument going into the function so the only data being input is the dictionary
    for value in dictionary:          # for loop takes the value of the argument and prints the value. Indexing has been removed from the function
        print(value)


simpson_catch_phrases = {"lisa": "BAAAAAART!",                     # changed layout of the dictionary so there is only one key and value per line
                         "bart": "Eat My Shorts!",                 # there was an extra ' in doh so it provided an unterminated string literal
                         "marge": "Mmm~mmmmm",                     # the extra ' made the closing curly brace unreadable
                         "homer": 'd''oh',
                         "maggie": "(Pacifier Suck)"}
dict_values = simpson_catch_phrases.values()                       # variable is created to assign only the values of the dictionary to

print_values_of(list(dict_values)[:2])                             # function is cast to a list as it is called so the values can be indexed
print_values_of(list(dict_values)[3:4])                            # the values of the dict_list are passed into the function as parameters


