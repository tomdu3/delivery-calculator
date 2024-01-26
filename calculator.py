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
MAX_DELIVERY_FEE = 15
MIN_DELIVERY_FREE = 200


def sur_charge(value):
    '''
    Takes the value of the cart and if it is less than 10
    returns the surplus charge of the difference to 10,
    otherwise no surplus charge
    '''
    return 0 if value >= MIN_CART_VALUE else 10 - value


def charge_distance(distance):
    if distance <= BASIC_DISTANCE:
        return BASIC_DISTANCE_CHARGE
    else:
        extra_charge = int(
            (distance - BASIC_DISTANCE - 1) / ADDITIONAL_DISTANCE + 1) *\
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


def friday_rush(order_date):
    rush_charge = 0
    datetime_object = datetime.fromisoformat(order_date)
    day = datetime_object.isoweekday()
    time = datetime_object.hour
    if day == 5 and 15 <= time <= 19:
        rush_charge = 1.2
    return rush_charge


def calculate_bill(data):
    amount = data['cart_value']
    distance = data['delivery_distance']
    number_of_items = data['number_of_items']
    time = data['time']
    if amount >= MIN_DELIVERY_FREE:
        delivery_fee = 0
    else:
        min_amount_charge = sur_charge(amount)
        distance_charge = charge_distance(distance)
        bulk_charge = charge_number_of_items(number_of_items)
        delivery_fee = (min_amount_charge + distance_charge + bulk_charge) *\
            friday_rush(time)
        delivery_fee = min(delivery_fee, MAX_DELIVERY_FEE)

    return amount + delivery_fee


print(calculate_bill(req_input))
