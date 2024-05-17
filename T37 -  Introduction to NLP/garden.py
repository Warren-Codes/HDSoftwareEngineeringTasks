import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathsentences = []

sentence1 = "The old man the boat."
sentence2 = "The complex houses married and single soldiers and their families."
sentence3 = "The horse raced past the barn fell."
sentence4 = "The florist sent the flowers was pleased."
sentence5 = "We painted the wall with cracks."
sentence6 = "The old Riaz Moola the boat."
sentence7 = "The horse raced past London fell."

# Each sentence will be added to the end of the gardenpathsentences list
gardenpathsentences += [sentence1, sentence2, sentence3, sentence4, sentence5, sentence6, sentence7]

# A new list to iterate over each sentence in gardenpathsentences list and put in the appropriate position tags.
pos_tags = []
for sentence in gardenpathsentences:
  doc = nlp(sentence)
  pos_tags.extend([(word.text, word.pos_) for word in doc])

print(pos_tags)
# 'man' in the first sentence appears as a noun but for the sentence to be grammatically correct it should be a verb.
# ' complex' in the second sentence appears as an adjective, but for it to be grammatically correct it should be a noun.

# A new list to iterate over each sentence in gardenpathsentences list and put in the appropriate entity tags.
nlp_ents = []
for sentence in gardenpathsentences:
  doc = nlp(sentence)
  nlp_ents.extend([(i, i.label_, i.label) for i in doc.ents])

print(nlp_ents)
# The entity list did not initially return anything, however, upon further reading it seems like this is because there
# no named entities were recognised by spaCy so I added Riaz and London to different sentences and that returned
# entitiy information. Am I right in thinking that the numbers are just the integer location of the string?