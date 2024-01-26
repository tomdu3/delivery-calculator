from datetime import datetime, timezone


req_input = {
    "cart_value": 790,
    "delivery_distance": 2235,
    "number_of_items": 4,
    "time": "2024-01-15T13:00:00Z"
}

MIN_CART_VALUE = 10
BASIC_DISTANCE_CHARGE = 2
ADDITIONAL_DISTANCE_CHARGE = 1
BASIC_DISTANCE = 1000
ADDITIONAL_DISTANCE = 500


def sur_charge(value):
    '''
    Takes the value of the cart and if it is less than 10
    returns the surplus charge of the difference to 10,
    otherwise no surplus charge
    '''
    return 0 if value >= MIN_CART_VALUE else 10 - value


def charge_distance(distance):
    if distance <= BASIC_DISTANCE: return BASIC_DISTANCE_CHARGE
    else:
        extra_charge = int((distance - BASIC_DISTANCE - 1)
            / ADDITIONAL_DISTANCE + 1) *\
            ADDITIONAL_DISTANCE_CHARGE
        total_charge = BASIC_DISTANCE_CHARGE + extra_charge
    return total_charge


def charge_number_of_items(number_of_items):
    total_charge = 0
    if number_of_items > 4:
        total_charge += (number_of_items - 4) * .50
        if number_of_items > 12:
            total_charge += 1.20
    return total_charge

# * The delivery fee can __never__ be more than 15€, including possible surcharges.
# * The delivery is free (0€) when the cart value is equal or more than 200€. 
# * During the Friday rush, 3 - 7 PM, the delivery fee (the total fee including possible surcharges) will be multiplied by 1.2x. However, the fee still cannot be more than the max (15€). Considering timezone, for simplicity, **use UTC as a timezone in backend solutions** (so Friday rush is 3 - 7 PM UTC). **In frontend solutions, use the timezone of the browser** (so Friday rush is 3 - 7 PM in the timezone of the browser).
def friday_rush(order_date):
    rush_charge = 0
    datetime_object = datetime.fromisoformat(order_date)
    day = datetime_object.isoweekday()
    time = datetime_object.hour
    if day == 5 and 15 <= time <= 19:
        rush_charge = 1.2
    return rush_charge

print(friday_rush(req_input['time']))

        
