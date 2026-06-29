import time


def setup_module(module):
    print("\nSetting up module %s" % module.__name__)


def teardown_module(module):
    print("\nTearing down module %s" % module.__name__)


def setup_function(function):
    print("\nSetting up for %s" % function.__name__)


def teardown_function(function):
    print("\nTearing down for %s" % function.__name__)


def testFunction1():
    print("Executing testFunction1")
    time.sleep(1)
    assert True


def testFunction2():
    print("Executing testFunction2")
    time.sleep(1)
    assert True


class TestClass:
    def testMethod1(self):
        print("Executing testMethod1")
        time.sleep(1)
        assert True

    def testMethod2(self):
        print("Executing testMethod2")
        time.sleep(3)
        assert True
