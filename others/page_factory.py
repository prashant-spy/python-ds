# Step 1: Define an abstract class or interface
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


# Step 2: Create concrete classes that implement the abstract class
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Step 3: Create a Factory Class with a factory method to generate objects
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


# Step 4: Client code that uses the factory to create objects
if __name__ == "__main__":
    # Create a Dog
    dog = AnimalFactory.create_animal("dog")
    print(dog.speak())  # Output: Woof!

    # Create a Cat
    cat = AnimalFactory.create_animal("cat")
    print(cat.speak())  # Output: Meow!
