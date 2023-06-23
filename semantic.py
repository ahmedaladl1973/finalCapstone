# Semantics comparison using both md and sd datasets
# By Ahmed AlAdl
# ----------------------------------------------------------------
# To test the difference you need to un-comment one of the loads first
# ----------------------------------------------------------------



import spacy
'''
# Load the medium pre-trianed NLP data model
nlp = spacy.load('en_core_web_md')

'''
# Load the small pre-trianed NLP data model
nlp = spacy.load('en_core_web_sd')


# Word comparison

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")


print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

# End of word comparison

#----------------------------------------------------------------

# Sentence comparison

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)

# End of sentence comparison
#----------------------------------------------------------------

'''My comments:

When using the sd data model the results swere are follows

  similarity = nlp(sentence).similarity(model_sentence)
where did my dog go -  0.4043351553824302
Hello, there is my car -  0.5648939507997681
I've lost my car in my car -  0.548028403302901
I'd like my boat back -  0.3007499696891998
I will name my dog Diana -  0.3904074310483232

When using the md data model the results were as follows

where did my dog go -  0.630065230699739
Hello, there is my car -  0.8033180111627156
I've lost my car in my car -  0.6787541571030323
I'd like my boat back -  0.5624940517078084
I will name my dog Diana -  0.6491444739190607

Since the traning data for the MD is larger than the SD, the results
were more accurate than the SD results.

'''