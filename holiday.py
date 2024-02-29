"""
Set a hotel cost per night
set a list of cities to be able to fly to 
Set a cost of care rental
Tell user how much hotel will cost
Tell user how much flight will cost
Tell user car rental will cost
Tell user how much the total cost of holiday is
Ask for user input on night sat hotel, where they are flying to
and how long they want to rent the car 
"""

# Setting hotel_cost per night with its parameter nights
def hotel_cost(nights):
    return nights * 100

# Setting list of cities to fly to and cost of flight with its parameter city
def plane_cost(city):
    if city.lower() == "paris":
        return 100
    elif city.lower() == "belgium":
        return 90
    elif city.lower() == "denmark":
        return 90
    elif city.lower() == "sydney":
        return 210
    elif city.lower() == "bangkok":
        return 200
    elif city.lower() == "venice":
        return 100

# Setting cost of car_rental per day with its parameter days
def car_rental(days):
    return days * 40

# Setting holiday_cost using the above parameters 
def holiday_cost(nights, city, days):
    # Setting hotel as hotel_cost with its parameter of nights 
    hotel = hotel_cost(nights)
    print("The cost for your hotel stay for", nights, "nights is: £", hotel)

    # Setting plane as plane_cost with its parameter of city
    plane = plane_cost(city)
    print("The cost of your plane ticket to", city, "is: £", plane)

    # Setting car as car_rental with it parameter days
    car = car_rental(days)
    print("The cost for your car rental for", days, "days is: £", car)
    
    # Setting total and calling on the parameters sett above
    total = hotel + plane + car
    # Print Total cost of holiday
    print("The total cost for your holiday is: £", total)




# Ask user how many nights staying in hotel changing answer from string to an integer
nights = int(input("How many nights would you like to stay at the hotel - "))
# Ask user which city they want to fly to 
city = input("Which city would you like to fly to?:\nParis\nBelgium\nDenmark\nSydney\nBangkok\nVenice\n- ")
# Ask user how many days they want to rent a car changing answer from a string to an integer
days = int(input("How many days would you like to rent a car for? - "))

holiday_cost(nights, city, days)