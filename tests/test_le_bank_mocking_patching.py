from datetime import datetime
from unittest.mock import patch, MagicMock

from src.le_bank import Customer

# Example using unittest MagicMock and patch
def test_transaction_with_mock_notifier():
    # Arrange
    # Mock the Notifier
    mock_notifier = MagicMock()
    sender = Customer("John", "Doe", starting_balance=100, notifier=mock_notifier)
    receiver = Customer("Jane", "Doe", starting_balance=100)
    
    # Act
    sender.make_transaction(receiver, 50)
    
    # Assert
    mock_notifier.notify.assert_called_once_with(sender, receiver, 50)
    
""" Patching Convention is peculiar and worth highlighting:

@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    MockClass1.return_value
    ....
    
    
## Where to patch
patch() works by (temporarily) changing the object that a name points to with another one. There can be many names pointing to any individual object, so for patching to work you must ensure that you patch the name used by the system under test.

The basic principle is that you patch where an object is looked up, which is not necessarily the same place as where it is defined. A couple of examples will help to clarify this.

Imagine we have a project that we want to test with the following structure:

a.py
    -> Defines SomeClass

b.py
    -> from a import SomeClass
    -> some_function instantiates SomeClass
Now we want to test some_function but we want to mock out SomeClass using patch(). The problem is that when we import module b, which we will have to do then it imports SomeClass from module a. If we use patch() to mock out a.SomeClass then it will have no effect on our test; module b already has a reference to the real SomeClass and it looks like our patching had no effect.

The key is to patch out SomeClass where it is used (or where it is looked up). In this case some_function will actually look up SomeClass in module b, where we have imported it. The patching should look like:

@patch('b.SomeClass')
However, consider the alternative scenario where instead of from a import SomeClass module b does import a and some_function uses a.SomeClass. Both of these import forms are common. In this case the class we want to patch is being looked up in the module and so we have to patch a.SomeClass instead:

@patch('a.SomeClass')

"""
# Example using pytest-mock and monkeypatch
@patch("src.le_bank.datetime")
def test_transaction_notification_formatted_correctly(mock_datetime):
    # Mock the Notifier
    fixed_time = datetime(2024, 1, 1, 12, 0, 0)
    mock_datetime.now.return_value = fixed_time
    
    mock_notifier = MagicMock()
    
    sender = Customer("John", "Doe", starting_balance=100, notifier=mock_notifier)
    receiver = Customer("Jane", "Doe", starting_balance=100)
    
    # Act
    sender.make_transaction(receiver, 50)
    
    # Assert
    mock_notifier.notify.assert_called_once_with(sender, receiver, 50)