string_characters = {}

user_string = input("Enter a sentence: ")

# for loop iterates for every character in user input and will add 1 each time a character occurs
for characters in user_string:
    if characters in string_characters:
        string_characters[characters] += 1

    else:
        string_characters[characters] = 1

print(str(string_characters))
