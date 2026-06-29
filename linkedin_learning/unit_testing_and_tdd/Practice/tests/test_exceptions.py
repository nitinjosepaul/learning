from pytest import raises

def raisesValueError():
    raise ValueError

def test_exception():
    with raises(ValueError):
        raisesValueError()