def test1():
    assert 5.0 == 5.0


def test2():
    assert 5.0 == 5.0


# This is the main file for execution.
if __name__ == '__main__':
    print('Starting main execution')
    for test in [test1, test2]:
        try:
            test()
        except AssertionError as e:
            print(f"{test.__name__} failed")
            raise
        else:
            print(f"{test.__name__} passed")

    print('Main execution finished')