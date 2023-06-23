# POS by Ahmed AlAl 23.4.2023

coffe_shop_menu_items_prices = {
    "coffee": 1.50,
    "tea": 1.00,
    "milk": 0.50,
    "sugar": 0.25,
    "water": 0.50,
    "milk_tea": 1.50,
    "Espresso": 2.00,
    "Cappuccino": 2.25,
    "Latte": 2.0,
    "Americano": 1.75, 
}
coffe_shop_menu_items = {  
    "coffee": 1.50,
    "tea": 1.00,
    "milk": 0.50,
    "sugar": 0.25,
    "water": 0.50,
    "milk_tea": 1.50,
    "Espresso": 2.00,
    "Cappuccino": 2.25,
    "Latte": 2.0,
    "Americano": 1.75,   
}
#Display the menu

def display_menu():
    print("\n")
    for item in coffe_shop_menu_items:
        print(f"{item}: {coffe_shop_menu_items[item]:.2f}")
    print("\n")

table_number = (input("What table number are you? "))
print(f"Welcome to the coffee shop, table {table_number}.")
print("\n")
print("Menu items:")
display_menu()

def get_order():
    full_order = {}
    continue_order = ""
    while continue_order != "n":
        display_menu()
        order = input("What would you like to order? ").lower()
        #if order not in coffe_shop_menu_items.keys():
         #   print("Item not avaible. Please try again.")
        order_quantity = int(input("How many would you like? "))
        continue_order=input("Would you like to order anything else? (y/n) ")
        full_order[order]=order_quantity
    if continue_order=="y":
        
        get_order()
    else :
          print(full_order)
    
get_order()



'''
def calculate_total(order, order_quantity):
    total = 0
    for i in order:
        item_value=coffe_shop_menu_items_prices[i]
        total_value+=item_value
    return total

order = get_order()

bill=calculate_total(order)

print(f"Your bill is ${bill:.2f}")

'''
