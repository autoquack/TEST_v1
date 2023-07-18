import datetime


class Dog:
    def bark(self):
        print(self.name)

my_pup = Dog()
my_pup.name = "Lara"
my_pup.bark()

neighbor_pup = Dog()
neighbor_pup.name = "Tara"
neighbor_pup.bark()


class Car:
    def age(self):
        print(datetime.datetime.today().year - self.year)
my_whip = Car()
my_whip.year = 2021
my_whip.age()