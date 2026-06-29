import pytest
from _pytest import mark

from checkout import Checkout

@pytest.fixture
def instantiateCheckout():
    co_obj = Checkout()
    co_obj.addItemPrice('Apple', 1)
    co_obj.addItemPrice('Banana', 2)
    return co_obj

def test_CanCalculateTotal(instantiateCheckout):
    instantiateCheckout.addItem('Banana')
    assert instantiateCheckout.calculateTotal() == 2

def test_GetCorrectTotalWithMultipleItems(instantiateCheckout):
    instantiateCheckout.addItem('Apple')
    instantiateCheckout.addItem('Banana')
    assert instantiateCheckout.calculateTotal() == 3

def test_CanAddDiscountRule(instantiateCheckout):
    instantiateCheckout.addDiscount('Apple', 3, 2)

def test_CanApplyDiscountRule(instantiateCheckout):
    instantiateCheckout.addDiscount('Apple', 3, 2)
    instantiateCheckout.addItem('Apple')
    instantiateCheckout.addItem('Apple')
    instantiateCheckout.addItem('Apple')
    instantiateCheckout.addItem('Apple')
    instantiateCheckout.addItem('Apple')
    assert instantiateCheckout.calculateTotal() == 4

def test_ExceptioWithUnlistedItem(instantiateCheckout):
    with pytest.raises(Exception):
        instantiateCheckout.addItem('Beans')