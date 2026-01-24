"""
Assignment:
Complete the BankAccount class.

1. Complete the constructor
    1. Set __account_number to account_number
    2. Set __balance to initial_balance
2. Complete the public getters
    1. Complete the get_account_number method to get the value of the private variable __account_number and return it.
    2. Complete the get_balance method to get the value of the private variable __balance and return it.
3. Complete the deposit method
    1. It should accept an amount as input and add it to the account balance.
    2. If the deposit amount isn't positive, it should raise a ValueError exception with the message cannot deposit zero or negative funds. Otherwise, it should add the amount to the balance.
4. Complete the withdraw method
    1. It should accept an amount and check if there is enough money in the account for the withdrawal.
    2. If the withdrawal amount isn't positive, it should raise a ValueError exception with the message cannot withdraw zero or negative funds.
    3. Then, if there are not enough funds it should raise a ValueError exception with the message insufficient funds.
    4. Otherwise, it should deduct the amount from the balance.
"""

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        if self.__balance < amount:
            raise ValueError("insufficient funds")
        self.__balance -= amount


