from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print(f"{self.name} is name")


class Dog(Animal):
    def sound(self):
        return "woo woo"


class Cat(Animal):
    def sound(self):
        return "meaw meaw"


if __name__ == '__main__':
    dog = Dog("Buddy")
    cat = Cat("cat")

    print(dog.sound())
    print(cat.sound())

    dog.sleep()
    cat.sleep()
