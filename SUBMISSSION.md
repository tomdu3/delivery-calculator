# Delivery Fee Calculator

**Wolt Summer 2024 Engineering Internships**
![Wolt Rendeer Coding](./docs/dall-e-backend-wolt.png)

Preliminary Assignment for backend internships.

- Django REST API Solution

[Original GitHub Repo with the Problem Docs](https://github.com/woltapp/engineering-internship-2024/tree/5a3edf8744925e9b20a58a1376ec20e998fad1e2)

## The Project Problem Statement
The goal of the assignment is to showcase your coding skills and ability to develop features. This is a highly important part of the hiring process so it's crucial to put effort into this without making it too bloated. Reviewers will put weight on three main aspects: code quality, maintainability, and testing. Based on the results of the assignment review, we will make the decision on proceeding to the technical interview.

Your task is to write a delivery fee calculator. This code is needed when a customer is ready with their shopping cart and we’d like to show them how much the delivery will cost. The delivery price depends on the cart value, the number of items in the cart, the time of the order, and the delivery distance.


### Specification
Rules for calculating a delivery fee
* If the cart value is less than 10€, a small order surcharge is added to the delivery price. The surcharge is the difference between the cart value and 10€. For example if the cart value is 8.90€, the surcharge will be 1.10€.
* A delivery fee for the first 1000 meters (=1km) is 2€. If the delivery distance is longer than that, 1€ is added for every additional 500 meters that the courier needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€.
  * Example 1: If the delivery distance is 1499 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
  * Example 2: If the delivery distance is 1500 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
  * Example 3: If the delivery distance is 1501 meters, the delivery fee is: 2€ base fee + 1€ for the first 500 m + 1€ for the second 500 m => 4€
* If the number of items is five or more, an additional 50 cent surcharge is added for each item above and including the fifth item. An extra "bulk" fee applies for more than 12 items of 1,20€
  * Example 1: If the number of items is 4, no extra surcharge
  * Example 2: If the number of items is 5, 50 cents surcharge is added
  * Example 3: If the number of items is 10, 3€ surcharge (6 x 50 cents) is added
  * Example 4: If the number of items is 13, 5,70€ surcharge is added ((9 * 50 cents) + 1,20€)
  * Example 5: If the number of items is 14, 6,20€ surcharge is added ((10 * 50 cents) + 1,20€)
* The delivery fee can __never__ be more than 15€, including possible surcharges.
* The delivery is free (0€) when the cart value is equal or more than 200€. 
* During the Friday rush, 3 - 7 PM, the delivery fee (the total fee including possible surcharges) will be multiplied by 1.2x. However, the fee still cannot be more than the max (15€). Considering timezone, for simplicity, **use UTC as a timezone in backend solutions** (so Friday rush is 3 - 7 PM UTC). **In frontend solutions, use the timezone of the browser** (so Friday rush is 3 - 7 PM in the timezone of the browser).

## Backend specifics

### Your task
Your task is to build an HTTP API which could be used for calculating the delivery fee.

Please use one of the programming languages available in the location you're applying to (Helsinki: Python / Kotlin & Berlin: Python / Kotlin / Scala). Feel free to use libraries / frameworks.

**Note that your technology choice here defines the scope of the possible technical interview and your focus area if starting to work at Wolt 😊**


### Specification
Implement an HTTP API (single POST endpoint) which calculates the delivery fee based on the information in the request payload (JSON) and includes the calculated delivery fee in the response payload (JSON).

#### Request
Example 1: 
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
```

##### Field details

| Field             | Type  | Description                                                               | Example value                             |
|:---               |:---   |:---                                                                       |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                                   |__790__ (790 cents = 7.90€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.      |__2235__ (2235 meters = 2.235 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.                   |__4__ (customer has 4 items in the cart)   |
|time               |String |Order time in UTC in [ISO format](https://en.wikipedia.org/wiki/ISO_8601). |__2024-01-15T13:00:00Z__                   |

#### Response
Example:
```json
{"delivery_fee": 710}
```

##### Field details

| Field         | Type  | Description                           | Example value             |
|:---           |:---   |:---                                   |:---                       |
|delivery_fee   |Integer|Calculated delivery fee __in cents__.  |__710__ (710 cents = 7.10€)|


#### Request
Example 2 (From the Front End Mockup Image): 
```json
{"cart_value": 20, "delivery_distance": 900, "number_of_items": 1, "time": "2021-10-21T13:00:00Z"}
```

##### Field details

| Field             | Type  | Description                                                               | Example value                             |
|:---               |:---   |:---                                                                       |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                                   |__2000__ (2000 cents = 2.00€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.      |__900__ (900 meters = 0.9 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.                   |__1__ (customer has 1 items in the cart)   |
|time               |String |Order time in UTC in [ISO format](https://en.wikipedia.org/wiki/ISO_8601). |__2021-10-21T13:00:00Z__                   |

#### Response
Example:
```json
{"delivery_fee": 200}
```

##### Field details

| Field         | Type  | Description                           | Example value             |
|:---           |:---   |:---                                   |:---                       |
|delivery_fee   |Integer|Calculated delivery fee __in cents__.  |__200__ (200 cents = 2.00€)|

## Django API Solution

### Technologies Used

- Python 3.12.1
- Django 5.0.1
- Django Rest Framework 3.14.0

### Django App Structure

- Django Project name - **calcdelivery**
- Django App - **delivery**
    - auxiliary script/module **calculator.py** - does the required calculations
    - serializer - deals with JSON conversion
    - tests - automated tests code

Complete directory structure can be seen below: 
  

<details>
<summary>Django App Directory Structure</summary>

```
.
├── calcdelivery
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── delivery
│   ├── admin.py
│   ├── apps.py
│   ├── auxiliary
│   │   ├── calculator.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── calculator.cpython-312.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── serializers.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── views.cpython-312.pyc
│   ├── serializers.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── tests_forms.cpython-312.pyc
│   │   │   ├── tests_serializers.cpython-312.pyc
│   │   │   ├── test_urls.cpython-312.pyc
│   │   │   └── test_views.cpython-312.pyc
│   │   ├── tests_serializers.py
│   │   ├── test_urls.py
│   │   └── test_views.py
│   ├── urls.py
│   └── views.py
├── docs
│   └── dall-e-backend-wolt.png
├── example-ui.png
├── manage.py
├── README.md
├── requirements.txt
├── SUBMISSSION.md
└── yuhos.png
```
</details>

### Database Model
A SQL(SQLite3) model was made for the Delivery.

| Key  | Name        | Type    | Extra Info                |
| ---- | ----------- | ------- | ------------------------- |
| PKey | id           | Integer | Unique id                 |
|      | cart_value   | Integer | Value of the shopping cart in cents.       |
|      | delivery_distance | Integer | The distance between the store and customer’s location in meters. |
|      | number_of_items | Integer   | The number of items in the customer's shopping cart. |
|      | time         | String  | Order time in UTC in ISO format. |
|      | delivery_fee | Integer | Description of event       |

### Calculator Module
The heart of the API is the Calculator module that is placed inside the `delivery/auxiliary` directory. It contains of one main calculating function and 4 additional functions that takes into account the required [specifications](#specification).

```
- calculate_delivery(amount, distance, number_of_items, time) - main function
    ├ sur_charge(value) -> surplus charge function
    ├ chage_distance(value) -> distance charge function
    ├ charge_number_of_items(number_of_items) -> number of items charge function
    └ friday_rush(order_date) -> if on Friday rush hours, charges +20%
```
### Serializer

The **DeliveryFeeSerializer** is primarily used to ensure that the data received through API requests for delivery-related operations are in the correct format and adhere to predefined validation rules. It plays a crucial role in data integrity and error handling in the context of an application dealing with delivery services.

### View

The **CalculateDeliveryFeeView** provides a robust API endpoint for clients to calculate delivery fees. It ensures that the input data is correctly formatted and valid through the *DeliveryFeeSerializer*, performs the necessary calculations through the *calculator* module, and handles both successful and erroneous scenarios appropriately, ensuring a clear and reliable communication via HTTP responses.

## Testing
### Automated tests




### API functionality
A default web interface loads when the server is running and can be accessed on http://localhost:8000/ in the browser (or in a API test software like Postman).
The allowed method is POST and the input data can be given through a form or as a raw JSON data structure. By clicking on the button POST the request is made and the calculated result is given.

<details>
<summary>Django REST Framework request and response</summary>

![Request](./docs/APIrequest.png)
![Response](./docs/APIresponse.png)

</details>



