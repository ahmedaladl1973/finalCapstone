# Task 5 by Ahmed AlAdl on 16.3.2023

# Define and input variable
full_name = input("Enter Your full name: ")

# Validation process

# Get the length of the full name
validate_full_name = (len(full_name))

# Proccing and output

# Check if the user entered nothing
if validate_full_name == 0 :
    print ("You haven't entered anything. Plese enter your full name")

# Check if the user entered a name with more than 24 characters
elif validate_full_name > 24 :
    print ("Make sure you only enter you full name only!")

# Check if the user entered a name with less than 3 characters or nothing
elif validate_full_name < 3 :
    print ("Entry too short. Plese enter your full name")

# Check if the user entered a full name
elif full_name.find(" ") == -1 :
    print ("Make sure you enter your full name!")



# Print the full name if the user entered a valid full name
else:
    print ("Thank you " + full_name +" for entering your full name!")
