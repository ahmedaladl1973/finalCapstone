# Purpose: To find the word type of a given word


import spacy

# Load the spacy model
nlp = spacy.load('en_core_web_sm')


# Get the text to be processed
text = "The world's biggest chocolate cake will be made for this Christmas by the Royal cake house."

# Create a document object from the text
doc = nlp(text)

# Iterate through the tokens in the document
for token in doc:
    print(token.text, token.pos_)

    