from __future__ import annotations
from typing import Union
from datetime import datetime

class Customer:
    def __init__(self, first_name: str, last_name: str, starting_balance: Union[int, float], notifier=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = starting_balance
        self.notifier = notifier  # optional notifier, which could be an email system
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}\nAccount Balance: £{self.balance:.2f}"
    
    def make_transaction(self, target_customer: 'Customer', amount: Union[int, float]):
        if amount < 0:
            raise ValueError("'amount' in transaction should be greater than 0")
        
        if amount > self.balance:
            raise ValueError("'amount' should be less than or equal to the balance")
        
        self.balance -= amount
        target_customer.balance += amount
        
        # Notify both the sender and the recipient
        if self.notifier:
            self.notifier.notify(self, target_customer, amount)


class Notifier:
    def notify(self, sender: Customer, recipient: Customer, amount: Union[int, float]):
        print(f"Notification: £{amount} transferred from {sender.first_name} to {recipient.first_name} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
