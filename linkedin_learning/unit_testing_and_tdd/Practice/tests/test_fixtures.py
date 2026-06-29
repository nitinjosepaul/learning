import pytest

@pytest.fixture
def setup():
    print("Set Up")

@pytest.fixture(autouse=True)
def teardown():
    print("Tear Down")

def test1(setup):
    print("Executing test1")
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2")
    assert True