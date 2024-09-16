import pytest
from src.le_bank import Customer


@pytest.fixture
def sender():
    return Customer("John", "Doe", 100)

@pytest.fixture
def receiver():
    return Customer("Jane", "Doe", 100)
        