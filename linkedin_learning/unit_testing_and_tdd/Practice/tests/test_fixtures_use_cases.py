import pytest

#######################################
# Setting up the test data
#######################################
class User:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def create_user():
    return User('John')

def test_user_name(create_user):
    assert create_user.name == 'John'


def test_user_type(create_user):
    assert isinstance(create_user, User)