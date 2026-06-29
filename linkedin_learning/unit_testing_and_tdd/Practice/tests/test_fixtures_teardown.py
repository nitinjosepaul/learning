import pytest

@pytest.fixture
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture
def setup2(request):
    print("\nSetup 2  ")

    def teardown_A():
        print("\nTeardown A")

    def teardown_B():
        print("\nTeardown B")

    request.addfinalizer(teardown_A)
    request.addfinalizer(teardown_B)

def test1(setup1):
    print("Executing test1")
    assert True

def test2(setup2):
    print("Executing test2")
    assert True
