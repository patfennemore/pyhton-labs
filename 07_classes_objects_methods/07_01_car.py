'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelerate(self):
        self.max_speed += 5

    def details(self):
        print(f"You car is a {self.model} which was made in {self.year} and has a max speed of {self.max_speed}")


ford = Car("Fiesta", 1998, 150)
nissan = Car("champ", 2002, 110)
nissan.accelerate()
nissan.details()
nissan.accelerate()
nissan.details()
