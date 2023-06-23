# Description: This program demonstrates how to extract sentences from a text using spaCy


import spacy

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

# Get the text to be processed
text = "The world's biggest chocolate cake will be made for this Christmas by the Royal cake house. The cake will be made with the finest ingredients and will be decorated with the most beautiful flowers. The cake will be a masterpiece and will be the talk of the town."

# Create a document object from the text
doc = nlp(text)

# Iterate through the sentences in the document
for sentence in doc.sents:
    print(sentence.text)