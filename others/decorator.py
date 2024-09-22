"""Decorators are functions that modify the behavior of other functions or methods without changing their code"""


def my_decorator(func):
    def wrapper(x):
        print("before function called")
        x += 5
        print("after function called")

    return wrapper


@my_decorator
def say_hello(x):
    print("hello!")
    return x


say_hello(5)
