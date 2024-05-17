# The first example defines days_of_week as a function and will print out the days of the week.
print("Example 1:")

def days_of_week(days):
    print(days)


days_of_week("Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday")

# -----------Example 2 --------------- #
print("\nExample 2:")

# replace(sentence) function turns the sentence into a list and splits it.
# enumerate(sentence_list) gives a counter for the sentence so it can be looped through
# modulus (%) 2  == 1 checks every second word in the list index
# every second word then gets replaced with " " and "hello" is joined next to it at the same index
def replace(sentence):
    sentence_list = sentence.split()
    for counter, word in enumerate(sentence_list):
        if counter % 2 == 1:
            sentence_list[counter] = "Hello"
    new_sentence = " ".join(sentence_list)
    print(new_sentence)

replace(input("Write your sentence: "))







