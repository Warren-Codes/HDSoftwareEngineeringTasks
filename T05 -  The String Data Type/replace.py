fox_string ="The!quick!brown!fox!jumps!over!the!lazy!dog!."

# This will replace all of the exclamation marks with an empty space. I don't know how to get rid of that one space before the full stop though, which you will see when it prints out.
rep_fox_string = fox_string.replace("!", " ") 
print(rep_fox_string)

# This will make the sentence be written out entirely in capital letters.
upper_fox_string = rep_fox_string.upper() 
print(upper_fox_string)

# Indexing is used to reverse the sentence. As there are 44 characters, the index starts on 44 and the : : denotes it goes until the end. the -1 tells the program to count back by 1 step each time.
print(rep_fox_string[44::-1])