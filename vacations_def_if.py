# using functions ( basic) and if-else statements
# taking a vacation using making decisions with if-elif. 
#Make you own scenario and create a program that display the cost of travel.

def hotel_cost(nights):
    return (140 * nights)


def plane_ride_cost(city):
    if city == 'Charlotte':
        return (183)
    elif city == 'Tampa':
        return (220)
    elif city == 'Pittsburgh':
        return (222)
    elif city == "Los Angeles":
        return (475)


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3 and days < 7:
        cost -= 20
    return cost


def trip_cost(city, days, spending_money):
    return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money


print(trip_cost("Los Angeles", 5, 600))
