
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

"""
def checkout(skus):
    # Check if the input is empty
    if not skus:
        return -1
    # Check if the input is a string
    if not isinstance(skus, str):
        return -1
    # Check if the input contains only valid SKUs
    if not all(sku in 'ABCD' for sku in skus):
        return -1
    # Check if the input contains only valid SKUs
    if not all(skus.count(sku) == 1 for sku in skus):
        return -1
    return -1


