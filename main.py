from src.le_bank import Customer
from src.le_bank import Notifier

notifier = Notifier()
john = Customer("John", "Smith", 10, notifier=notifier)
jane = Customer("Jane", "Smith", 10)

print(john)
print(jane)

john.make_transaction(jane, 5)

print(john)
print(jane)