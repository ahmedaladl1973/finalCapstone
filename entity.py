import spacy

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

# Get the text to be processed
text = "The world's biggest chocolate cake will be made for this Christmas by the Royal cake house."

# Create a document object from the text
doc = nlp(text)

# Find all entities in the document
for entity in doc.ents:
    print(entity.text, entity.label_)
