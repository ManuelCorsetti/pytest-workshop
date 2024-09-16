import pytest
from src.le_bank import Customer

class TestCustomerDunderStr:
    def test_correct_output_shown_positive_balance(self):
        message = "Smith, John\nAccount Balance: £10.00"
        customer = Customer("John", "Smith", 10)

        assert message == customer.__str__()
        
    @pytest.mark.xfail
    def test_negative_balance(self):
        message = "Jane, Doe\nAccount Balance: -£10.00"
        customer = Customer("Doe", "Jane", -10)

        assert message == customer.__str__()
        
    def test_zero_balance(self):
        message = "Jane, Doe\nAccount Balance: £0.00"
        customer = Customer("Doe", "Jane", 0)

        assert message == customer.__str__()
        

class TestMakeTransaction:
    # good examples using parameterize
    @pytest.mark.parametrize("amount, result", [
        (10, 90),
        (20, 80),
        (100, 0),
    ])
    def test_source_customer_end_balance(self, amount, result):
        sender = Customer("John", "Doe", 100)
        receiver = Customer("Jane", "Doe", 100)
        
        sender.make_transaction(receiver, amount=amount)
        
        assert result == sender.balance
        
    @pytest.mark.parametrize("amount, result", [
        (10, 110),
        (20, 120),
        (100, 200),
    ])
    def test_target_customer_end_balance(self, amount, result):
        sender = Customer("John", "Doe", 100)
        receiver = Customer("Jane", "Doe", 100)
        
        sender.make_transaction(receiver, amount=amount)
        
        assert result == receiver.balance
        
    # edge case - transact just enough money
    def test_sends_all_balance(self):
        sender = Customer("John", "Doe", 100)
        receiver = Customer("Jane", "Doe", 100)
        
        sender.make_transaction(receiver, amount=100)
        
        assert 200 == receiver.balance
        
    # bad case - transact negative money
    def test_negative_value_transaction_raises_errror(self):
        with pytest.raises(ValueError):
            sender = Customer("John", "Doe", 100)
            receiver = Customer("Jane", "Doe", 100)
            
            sender.make_transaction(receiver, amount=-100)
        
    # bad case - transact not enough money
    def test_transaction_greater_than_balance(self):
        sender = Customer("John", "Doe", 100)
        receiver = Customer("Jane", "Doe", 100)
        
        with pytest.raises(ValueError):
            sender.make_transaction(receiver, amount=101)