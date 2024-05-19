# noinspection PyUnusedLocal
# skus = unicode string
"""
The purpose of this challenge is to implement a supermarket checkout that calculates
 the total price of a number of items.

In a normal supermarket, things are identified using Stock Keeping Units, or SKUs.
In our store, we'll use individual letters of the alphabet (A, B, C, and so on).
Our goods are priced individually. In addition, some items are multi-priced: buy n of them, and they'll cost you y pounds.
For example, item A might cost 50 pounds individually, but this week we have a special offer:
 buy three As and they'll cost you 130.

Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+


Notes:
 - For any illegal input return -1

In order to complete the round you need to implement the following method:
     checkout(String) -> Integer

Where:
 - param[0] = a String containing the SKUs of all the products in the basket
 - @return = an Integer representing the total checkout value of the items

ROUND 2 - More offers
The checkout feature is great and our supermarket is doing fine. Is time to think about growth.
Our marketing teams wants to experiment with new offer types and we should do our best to support them.

We are going to sell a new item E.
Normally E costs 40, but if you buy 2 of Es you will get B free. How cool is that ? Multi-priced items also seemed to work well so we should have more of these.

Our price table and offers:
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+


Notes:
 - The policy of the supermarket is to always favor the customer when applying special offers.
 - All the offers are well balanced so that they can be safely combined.
 - For any illegal input return -1
"""


def checkout(skus: str):
    price_table = {
        'A': {'price': 50, 'offers': [{'quantity': 3, 'price': 130}, {'quantity': 5, 'price': 200}]},
        'B': {'price': 30, 'offers': [{'quantity': 2, 'price': 45}]},
        'C': {'price': 20, 'offers': []},
        'D': {'price': 15, 'offers': []},
        'E': {'price': 40, 'offers': [{'quantity': 2, 'free': 'B'}]}
    }
    if not skus:
        return 0
    if not all(sku in price_table for sku in skus):
        return -1

    total_price = 0
    basket = {sku: skus.count(sku) for sku in set(skus)}

    for sku, quantity in basket.items():
        price = price_table[sku]['price']
        offers = price_table[sku]['offers']

        for offer in sorted(offers, key=lambda x: -x.get('quantity', 0)):
            while quantity >= offer.get('quantity', 0):
                if 'price' in offer:
                    total_price += offer['price']
                    quantity -= offer['quantity']
                elif 'free' in offer and basket.get(offer['free'], 0) == 1:
                    basket[offer['free']] -= 1
                    total_price -= price_table[offer['free']]['price']
                quantity -= offer['quantity']

        total_price += price * quantity

    return total_price


