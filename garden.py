# The Garden Path Sentencees
# By Ahmed AlAdl

import spacy

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

# Get the text to be processed
text = ["The horse raced past the barn fell.",
    "The old man the boat.",
    "Visiting relatives can be boring.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
] 

# Create a document object from the text
#documents = []
for sentence in text:
  doc = nlp(sentence)
  #documents.append(doc)
  for token in doc:
    print(token, token.pos_)

# Get an explanation of AUX entity and print it
entity_fac = spacy.explain("AUX")
print(f"AUX:{entity_fac}")

# Get an explanation of ADP entity and print it
entity_fac = spacy.explain("ADP")
print(f"ADP:{entity_fac}")

'''
--------------------------------------------------------
I looked up the entities ADP and AUX.
Both entities made sense.
--------------------------------------------------------
'''