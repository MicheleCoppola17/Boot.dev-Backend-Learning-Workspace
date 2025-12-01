"""
Assignment:
Complete the purchase_item function.

1. If the character doesn't have enough gold raise an Exception with the text not enough gold.
2. Otherwise, return the amount of remaining money the customer has after completing the purchase.

Do not handle the exception, the test file does that for you.
"""

def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    else:
        return gold_available - price
