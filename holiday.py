# Task 14 by Ahmed AlAdl 1.4.2023


# Define lists and Dictionaires

cities_flight_cost={"london":300,
        "paris":400,
        "new york":500,
        "dubai":600,
        "tokyo":800,
        "Sydney":1000,
        "melbourne":1000,
        "cairo":500,
        "rome":300,
        "madrid":300}

city_hotel_cost_per_night={"london":100,
        "paris":100,
        "new york":200,
        "dubai":200,
        "tokyo":300,
        "sydney":300,
        "melbourne":300,
        "cairo":200,
        "rome":100,
        "madrid":100}

car_rental_cost_per_day={"london":50,
        "paris":50,
        "new york":100,
        "dubai":100,
        "tokyo":150,
        "sydney":150,
        "melbourne":150,
        "cairo":100,
        "rome":50,
        "madrid":50}

# Define the cost of the trip fucntion
def cost_of_trip(user_distination,user_days,user_car):
    flight_cost=cities_flight_cost[user_distination]
    hotel_cost=city_hotel_cost_per_night[user_distination]*user_days
    if user_car=="yes" : 
        car_cost=car_rental_cost_per_day[user_distination]*user_days
    else:
        car_cost=0
    total_cost=flight_cost+hotel_cost+car_cost
    return total_cost


# Main Screen and menu

menu_choice = 0
while menu_choice != 1:
    print(("#")*50)
    print("Welcome to the Holiday Planner")
    print(("#")*50)
    print()
    print("Destinations:")
    print("London" + " "*5 + "Paris" + " "*5 + "New York" + " "*5 + "Dubai" + " "*5 + "Tokyo" + " "*5 + "Sydney" + " "*5 + "Melbourne" + " "*5 + "Cairo" + " "*5 + "Rome" + " "*5+ "Madrid")
    print()
    


    # Input user distination and days

    user_distination_input=input("Enter your distination: ")

    # Validate the user distination
    while user_distination_input not in cities_flight_cost:
        print("Distination not available")
        user_distination_input=input("Enter another distination: ")
        user_distination=user_distination_input.lower()
    
    # Validate and enter the number of days
    try:
        user_days=int(input("Enter the number of days: "))
    except ValueError:
        print("Invalid number of days")
        user_days=int(input("Enter the number of days: "))

    # Validate and enter rental car
    user_car_input=input("Do you want a car? (yes/no)" )        
    while user_car_input not in ("yes","no","y","n"):
        print("Invalid input enter yes or no")
        user_car_input=input("Do you want a car? (yes/no)" )

    # Convert the user input to lower case
    user_distination=user_distination_input.lower()
    user_car=user_car_input.lower()
       
    # Calculate the cost of the trip
    cost_of_trip(user_distination,user_days,user_car)

    # Output the cost of the trip
    print("Flight cost: " + str(cities_flight_cost[user_distination]))
    print("Hotel cost: " + str(city_hotel_cost_per_night[user_distination]*user_days))
    if user_car=="yes" or user_car=="y":
            print("Car cost: " + str(car_rental_cost_per_day[user_distination]*user_days))
    print("The cost of the trip is: " + str(cost_of_trip(user_distination,user_days,user_car)))

    #Exit the program 
    menu_choice=int(input("Press 2 to try another distination or 1 for Exit "))      
    if menu_choice == 1:
        print("Safe Trip")
                                    




                           




