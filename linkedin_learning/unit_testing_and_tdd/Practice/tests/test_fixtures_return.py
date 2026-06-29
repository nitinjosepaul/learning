import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    return_value = request.param
    print("Setup : Returning {}".format(return_value))
    return return_value

def test1(setup):
    print("Executing test1 with {}".format(setup))
    assert True