class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Животное издает звук"


class Dog(Animal):
    def speak(self):
        return f"{self.name} лает"


dog = Dog("Бобик")
print(dog.speak())