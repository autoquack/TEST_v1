class Animal:
    def __init__(self, breed, color, weight):
        self.breed = breed
        self.color = color
        self.weight = weight

    def walk(self):
        print("I am walking")

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")


class Dog(Animal):
    def eat(self):
        print("I am eating like a dog, messy!")

    def bark(self):
        print("I am barking")


class Cat(Animal):
    def eat(self):
        print("I am eating like a cat")

    def meow(self):
        print("I am meowing")


class DetectDrugsMixin:
    def detect_drugs(self):
        print("I am detecting some drugs here!")


class PoliceDog(Dog, DetectDrugsMixin):
    def __init__(self, breed, color, weight, hours_on_mission):
        super().__init__(breed, color, weight)
        self.hours_on_mission = hours_on_mission


def make_animal_eat(animal):
    animal.eat()


if __name__ == "__main__":
    blue_cat = Cat("british shorthair", "blue", 7000)
    golden_dog = Dog("golden retriever", "golden", 5000)

    make_animal_eat(blue_cat)
    make_animal_eat(golden_dog)


