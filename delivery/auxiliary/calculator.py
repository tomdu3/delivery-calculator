"""
Main calculating app added as an auxiliary code to the django project
"""

from datetime import datetime, timezone

MIN_CART_VALUE = 1000  # 10€
BASIC_DISTANCE_CHARGE = 200  # 2€
ADDITIONAL_DISTANCE_CHARGE = 100  # 1€
BASIC_DISTANCE = 1000  # 1km
ADDITIONAL_DISTANCE = 500  # 0.5km
MAX_DELIVERY_FEE = 1500  # 15€
MIN_DELIVERY_FREE = 20000  # 200€


def sur_charge(value):
    """
    Takes the value of the cart and if it is less than 10Eur
    returns the surplus charge of the difference to 10Eur,
    otherwise no surplus charge
    """

    return 0 if value >= MIN_CART_VALUE else MIN_CART_VALUE - value


def charge_distance(distance):
    """
    Calculates delivery charges according to the distance
    """
    # returns the basic charge for the value uptil a defined basic distance
    if distance <= BASIC_DISTANCE:
        return BASIC_DISTANCE_CHARGE
    else:
        # adds extra charge for every additional distance unit treshold
        extra_charge = (
            int((distance - BASIC_DISTANCE - 1) / ADDITIONAL_DISTANCE + 1)
            * ADDITIONAL_DISTANCE_CHARGE
        )
        total_charge = BASIC_DISTANCE_CHARGE + extra_charge
    return total_charge


def charge_number_of_items(number_of_items):
    """
    Calculates and returns the charges depending on the number of items:
    Under minimum number, bulk, ...
    """
    total_charge = 0
    if number_of_items > 4:
        # adds aditional charge for every item over basic 4
        total_charge += (number_of_items - 4) * 50
        if number_of_items > 12:
            # adds a bulk fee for the order with more than 12 items
            total_charge += 120
    return total_charge


def friday_rush(order_date):
    """
    Checks if the given day is Friday and if the time slot is between
    3pm and 7pm and calculates and returnes the extra charges accordingly
    """

    rush_charge = 1  # default normal delivery charge
    # calculates the day of the week from the date string
    datetime_object = datetime.fromisoformat(order_date)
    day = datetime_object.isoweekday()
    time = datetime_object.hour
    # if the day is Friday and the rush hours time, extra charge is calculated
    if day == 5 and 15 <= time <= 19:
        rush_charge = 1.2
    return rush_charge


def calculate_delivery(amount, distance, number_of_items, time):
    """
    Main function. Calculates and returns the total of the delivery fee.
    It waves all charges (delivery and other fees) if the value of the order
    is of 200 or more.
    It doesn't go over 15Eur for the sum of delivery and other charges.
    """

    # if the cart value is greater or equal to the minimal free delivery,
    # there are no extra charges for delivery and other services
    if amount >= MIN_DELIVERY_FREE:
        delivery_fee = 0
    else:
        # calculates extra charges and delivery costs
        min_amount_charge = sur_charge(amount)
        distance_charge = charge_distance(distance)
        bulk_charge = charge_number_of_items(number_of_items)
        # total of the fees
        delivery_fee = (
            min_amount_charge + distance_charge + bulk_charge
        ) * friday_rush(time)
        # not overpassing the alowed fee amount
        delivery_fee = int(min(delivery_fee, MAX_DELIVERY_FEE))

    return {"delivery_fee": delivery_fee}


if __name__ == "__main__":
    # function call runs directly when the script is not imported as a module

    # sample input
    cart_value = 790
    delivery_distance = 2235
    number_of_items = 4
    time = "2024-01-15T13:00:00Z"

    print(calculate_delivery(cart_value, delivery_distance, number_of_items, time))

    input_data = {
        "cart_value": 2000,
        "delivery_distance": 900,
        "number_of_items": 1,
        "time": "2021-10-21T13:00:00Z",
    }
    print(
        calculate_delivery(
            amount=input_data["cart_value"],
            distance=input_data["delivery_distance"],
            number_of_items=input_data["number_of_items"],
            time=input_data["time"],
        )
    )
