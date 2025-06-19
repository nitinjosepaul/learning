def check_non_negative(key):
    def validator(f):
        def wrap(**kwargs):
            if kwargs[key] < 0:
                raise ValueError("Argument {} must be non-negative".format(key))
            return f(**kwargs)
        return wrap
    return validator


@check_non_negative("size")
def create_list(value, size):
    return [value] * size


print(create_list(value='a', size=3))
print(create_list(value='a', size=-1))