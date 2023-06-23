# Take 9 by Ahmed AlAdl 3.4.2023
# Difine the functions

# Import libraries
import os

# Add function
def add(x,y):
    return x + y

# Subtraction function
def subtaction(x,y):
    return x - y

# Multiplication function
def multiply(x,y):
    return x * y

# Division function
def divide(x,y):
    return x / y

# Input file name and vaidate it
while True:
    filename = input("Enter a file name to store your calculations: ")
    # Check if the file name contains any numbers
    try :
        if not filename.isalpha():
            print("The file name must contain only letters.")
            continue   
    except:
            break

    # Check if the file exists
    if os.path.exists(filename):
        file_choice = input("The file {} already exists. Would you like to overwrite it (O) or create a new file (N)?".format(filename))
        # Check if the user entered O or N
        while file_choice not in ["O", "N"]:
            print("Invalid choice. Please enter O or N.")
            file_choice = input("The file {} already exists. Would you like to overwrite it (O) or create a new file (N)?".format(filename))
        # Check if the user wants to overwrite the file
        if file_choice == "O":
            with open(filename, 'w') as filewrite:
                filewrite.write("")
                print("The file {} has been overwritten.".format(filename))
            break
        # Check if the user wants to create a new file
        elif file_choice == "N":
            while True:
                filename = input("Enter another file name to store your calculations: ")
                # Check if the file name contains only letters, this is another way to do it
                for char in filename:
                    if not char.isalpha():
                        print("The file name must contain only letters.")
                        continue
                    else:
                        break
                # Create the new file if the file name is was not valid the first time        
                with open(filename, 'w') as filewrite:
                    filewrite.write("")
                    print("The file {} has been created.".format(filename))
                    break
            break
    else:
        # Create the new file
        with open(filename, 'w') as filewrite:
            filewrite.write("")
        print("The file {} has been created.".format(filename))
        break

# Operation selction menu
print("Select operation : ")
print("+")
print("-")
print("/")
print("*")

# Loop to keep the menu running
menu_choice = 0
while menu_choice != 3:
        # Take input from the user
        try:
                choice = input("Enter Operation : ")
                # Valedate if choice is one of the four options
        except ValueError:
                     print("Invalid input. Please enter a valed operation")
                     continue
        # Check if choice is one of the four options
        if choice in ("+", "-" ,"/" ,"*"):
               # Inout numbers
                try:
                     num1 = float(input("Enter first number :"))
                     num2 = float(input("Enter second number :"))
                except ValueError:
                     print("Invalid input. Please enter a number")
                     continue
                
                # Addition operation     
                if choice == "+":
                     print(num1, "+", num2, "=", add(num1, num2))
                     # Create file
                     with open(filename, 'a') as file_write:
                         # Disply results and write the result to a file
                         print(num1, "+", num2, "=", add(num1, num2), file=file_write)

                # Subtraction operation
                elif choice == "-":
                     print(num1, "-", num2, "=", subtaction(num1, num2))
                     # Create file
                     with open(filename, 'a') as file_write:
                         # Disply results and write the result to a file
                         print(num1, "-", num2, "=", subtaction(num1, num2), file=file_write)
                # Division operation
                elif choice == "/":
                    try:
                     print(num1, "/", num2, "=", divide(num1, num2))
                     # Validate if user is trying to divide by zero
                    except ZeroDivisionError:
                        print("Division by zero is not allowed")
                        continue
                     # Create file
                    with open(filename, 'a') as file_write:
                         # Disply results and write the result to a file
                         print(num1, "/", num2, "=", divide(num1, num2), file=file_write) 

                # Multiplication operation
                elif choice == "*":
                     print(num1, "*", num2, "=", multiply(num1, num2))
                     # Create file
                     with open(filename, 'a') as file_write:
                        # Disply results and write the result to a file
                         print(num1, "*", num2, "=", multiply(num1, num2), file=file_write) 
                
                # Ask user if they want to try another operation or print last operation or Exit
                menu_choice=int(input("Press 1 to try another operation or 2 to print opperations and exit or 3 for Exit "))
                
                # Disply last operation from file
                if menu_choice == 2:
                    with open(filename, 'r') as file_read:
                        print(file_read.read())
                    break
                 



