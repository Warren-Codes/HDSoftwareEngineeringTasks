# TASK 1
print("\nTask 1:")
def add_prefix_un(word):
  return "un" + word

print(add_prefix_un("happy"))
print(add_prefix_un("able"))
print(add_prefix_un("certain"))

# TASK 2
print("\nTask 2:")
def make_word_groups(vocab_words):
  prefix = vocab_words[0]
  words = vocab_words[1:]
  prefixed_words = []
  for word in words:
    prefixed_words.append(prefix + word)
  return prefix + " :: " + " :: ".join(prefixed_words)

print(make_word_groups(["en", "close", "velop", "circle"]))
print(make_word_groups(["pre", "sent", "dict", "pare"]))
print(make_word_groups(["auto", "nomous", "biography", "immune"]))
print(make_word_groups(["inter", "view", "national", "mediate"]))

# TASK 3
print("\nTask 3:")
def remove_suffix_ness(word):
  if word.endswith("iness"):
    return word[:-5] + "y"
  elif word.endswith("ness"):
    if word[-5] == "i":
      return word[:-4] + "y"
    else:
      return word[:-4]
  else:
    return word

print(remove_suffix_ness("happiness"))
print(remove_suffix_ness("darkness"))
print(remove_suffix_ness("loneliness"))
print(remove_suffix_ness("forgiveness"))

# TASK 4
print("\nTask 4:")
def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    verb = adjective + "en"
    return verb


sentence = "The room was dark"
index = 3

verb = adjective_to_verb(sentence, index)
print(verb)



