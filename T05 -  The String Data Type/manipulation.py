# The user needs to write their own sentence and the len command will display the amount of characters in the sentence.
str_manip = input("Please write a sentence but don't include a fullstop :) ")
print(len(str_manip))

# This will find the last letter of the sentence and replace it, and all of the same letters in the sentence, with @.
last_char_string = str_manip.replace(str_manip[-1],"@")
print(last_char_string)

# The last three letters of the sentence will be printed in reverse. Remember the syntax for indexing is start: stop: steps. So this will start on the last character -1 
# and stop while including the 3rd character -4 with a step of counting back in ones shown as -1
# This is shown as -1:-4:-1
print(str_manip[-1:-4:-1])

# These are character variables which store the first 3 and last 2 characters of the user's string. Remember that computers first character is defined as 0 so the first three are 0, 1, 2 
# and the last two are -2, -1
char1 = str_manip[0]
char2 = str_manip[1]
char3 = str_manip[2]
char4 = str_manip[-2]
char5 = str_manip[-1]

print(char1 + char2 + char3 + char4 + char5) 

