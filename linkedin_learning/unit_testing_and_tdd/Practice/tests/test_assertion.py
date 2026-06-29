from pytest import approx

def test_intAssert():
    assert 1 == 1

def test_StrAssert():
    assert "str" == "str"

def test_floatAssert():
    assert 0.1 + 0.2 == approx(0.3)

def test_arrayAssert():
    assert [1,2,3] == [1,2,3]

def test_dictAssert():
    assert {'1':1} == {'1':1}
