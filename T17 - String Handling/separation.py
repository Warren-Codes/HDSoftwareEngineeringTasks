# The user is asked to input a sentence
# sentence.replace is used to replace the space with \n which makes each word go onto a new line
sentence = (input("Please type in a sentence:   "))
sentence = sentence.replace(" ", "\n")
print(sentence)