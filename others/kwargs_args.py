def dynamic_function(*args, **kwargs):
    for i, arg in enumerate(args):
        print(f"argument {i} : {arg}")

    for key, value in kwargs.items():
        print(f"{key}:{value}")


def immutable(string):
    string += "" + string

    print(string)


if __name__ == '__main__':
    # dynamic_function(1, 2, 3, 4)
    dynamic_function(name="peter", age=30, city="new york")
    immutable("test")
