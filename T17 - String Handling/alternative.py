# -------------- Example 1 ----------#

# A sentence list has been created with each character being alternate upper and lower case
# The sentence list was joined using .join function so the characters appear as words.
example1_list = ["E", "x", "A", "m", "P", "l", "E", " ", "1", ":"]
example1_joined = "".join(example1_list)
print(example1_joined)

sentence_list = ["h", "E", "l", "L", "o", " ", "W", "o", "R", "l", "D", " ", "t", "H", "i", "S", " ", "i", "S", " " "l", "O", "n", "D", "o", "N", " ", "c", "A", "l", "L", "i", "N", "g"]
sentence_joined = "".join(sentence_list)
print(sentence_joined)

#------------Example 2 ----------#
print("\nExample 2:")
# Each word in the list has been idexed and assigned alternate upper and lower case.
word1 = sentence_joined.upper()[0:5]
word2 = sentence_joined.lower()[6:11]
word3 = sentence_joined.upper()[12:16]
word4 = sentence_joined.lower()[17:19]
word5 = sentence_joined.upper()[20:26]
word6 = sentence_joined.lower()[27:34]

# A sentence list has been made with the alternate upper and lower case words
# These words have then been joined using the .join command to create a sentence string with alternate upper and lower case words
sentence2_list = [word1, word2, word3, word4, word5, word6]
sentence2_joined = " ".join(sentence2_list)
print(sentence2_joined) 

