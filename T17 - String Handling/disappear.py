user_sentence = (input("Please write a sentence:    "))

# A whiile loop is instigated which will keep asking the user to type in the letter they want to omit. If they do not wish to omit any other letters then the need to type -1
# A for loop is nested within the while loop. The for loop will replace all of the letters inputted in the disappear_question  and replace them with nothing, shown by using ""

# Python 3.8 introduced the walrus operator so I've used it here!
# The walrus operator is := to resemble eyes and tusks. It allows for two commands to be given in one line of code instead of two. The code asks the user for an input and it also includes the != "-1"
# to allow the user to type "-1" to get out. This is the equivalent of typing if disappear_question == "-1": print(user_sentence)
while (disappear_question := input("What character would you like to make disappear?  ")) != "-1":

    for letters in disappear_question:
        user_sentence = user_sentence.replace(letters, "")

print(user_sentence)

# After writing this code and ensuring that the user keeps getting asked what character to omit, I realised that all of the characters can inputted during the first "What character would you like to make disappear
# question." The problem is, if the user inputs a space, then all of the spaces in the new sentence also get omitted.
