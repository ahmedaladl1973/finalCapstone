# Task 12 by Ahmed AlAdl 1.4.2023


# Define lists and Dictionaires

menu=["Cappuccino","Latte","Espresso","Americano","Mocha","Cafe Mocha","Cafe Latte","Cafe au Lait","Cafe Bombon"]
price={"Cappuccino":3.5,"Latte":3.5,"Espresso":2.5,"Americano":2.5,"Mocha":3.5,"Cafe Mocha":3.5,"Cafe Latte":3.5,"Cafe au Lait":3.5,"Cafe Bombon":3.5}
stock={"Cappuccino":10,"Latte":10,"Espresso":10,"Americano":10,"Mocha":10,"Cafe Mocha":10,"Cafe Latte":10,"Cafe au Lait":10,"Cafe Bombon":10}
total_value=0

# Difineing the menu choice

menu_choice = 0
while menu_choice != 4:
    print()
    print("1. Show Menu with prices")
    print("2. Show item stock")
    print("3. Show total stock value")
    print("4. Exit")
   
    menu_choice = int(input("Menu Choice (1-4): "))
 
# Operations for the menu choice
# Output for the menu choice
  
    if menu_choice == 1:
       print("Items and Prices")
       for i in price:
            print(i,price[i])
    elif menu_choice == 2:
        print("Items and Stock")
        for y in stock:
            print(y,stock[y])
    elif menu_choice == 3:
        for items in menu:   
            item_value=(stock[items]*price[items]) 
            total_value+=item_value
           
        print()
        print("Total Stock Value: "+str(total_value))

# Exit the program       
if menu_choice == 4:
        print("Goodbye!")

