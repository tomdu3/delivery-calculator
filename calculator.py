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


# * If the number of items is five or more, an additional 50 cent surcharge is added for each item above and including the fifth item. An extra "bulk" fee applies for more than 12 items of 1,20€
#   * Example 1: If the number of items is 4, no extra surcharge
#   * Example 2: If the number of items is 5, 50 cents surcharge is added
#   * Example 3: If the number of items is 10, 3€ surcharge (6 x 50 cents) is added
#   * Example 4: If the number of items is 13, 5,70€ surcharge is added ((9 * 50 cents) + 1,20€)
#   * Example 5: If the number of items is 14, 6,20€ surcharge is added ((10 * 50 cents) + 1,20€)

def charge_number_of_items(number_of_items):
    total_charge = 0
    if number_of_items > 4:
        total_charge += (number_of_items - 4) * .50
        if number_of_items > 12:
            total_charge += 1.20
    return total_charge



