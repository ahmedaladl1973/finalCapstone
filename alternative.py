# Task 11 By Ahmed AlAdl 1.4.2023

#Change te case of every other letter in a sentence
# Difining and initializing variables

orginal_sentence = input("Enter you sentnce :") 
final_sentence = ""

for i in range(len(orginal_sentence)):
    if i % 2 == 0:
        final_sentence += orginal_sentence[i].upper()
    else:
        final_sentence += orginal_sentence[i].lower()

# Output
print(final_sentence)

# Chnage the case of every other word in a sentence
# Difining and initializing variables

orginal_phrase = str(input("Enter you sentnce :")).split()
final_phrase = " "

for i in range(len(orginal_phrase)):
    if i % 2 == 1:
        final_phrase += orginal_phrase[i].upper() + " "
    else:
        final_phrase += orginal_phrase[i].lower() + " "


# Output
print(final_phrase)