def hotel_cost(night):
    return 140*night

def plane_ride_cost(city):
    if "Charlotte"== city:
        return 183
    elif "Tampa"== city:
        return 220
    elif "Pittsburgh"== city:
        return 222
    elif "Los Angeles"== city:
        return 475
    
def rental_car_cost(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days
    
def trip_cost(city,days,spending_money):
        return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
city=input("Enter the city (Charlotte,tampa,pittsburgh,los angeles) : ")
days=int(input("Enter number of days you will stay : "))
spending_money=int(input("Enter extra spending money: "))

print("Cost  of car  rental:",rental_car_cost(days))
print("Cost of hotel room:", hotel_cost(days))
print("Cost of plane ride:", plane_ride_cost(city))
print("total cost of the trip: ", trip_cost(city,days,spending_money))