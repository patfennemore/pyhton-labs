'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class Vehicle:
    def __init__(self, model, year, speed):
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self):
        return f"{self.model} goes at {self.speed} and was made in {self.year}"


class Truck(Vehicle):
    def __init__(self, model, year, speed, weight):
        Vehicle.__init__(self, model, year, speed)
        self.weight = weight

    def __str__(self):
        return f"{Vehicle.__str__(self)} and weighs {self.weight}kg"


class Motorcycle(Vehicle):
    def __init__(self, model, year, speed, cc):
        Vehicle.__init__(self, model, year, speed)
        self.cc = cc

    def __str__(self):
        return f"{Vehicle.__str__(self)} and has an engine with {self.cc}cc"


class OffRoadMotorBike(Motorcycle):
    def __init__(self, model, year, speed, cc, suspension):
        Motorcycle.__init__(self, model, year, speed, cc)
        self.suspension = suspension

    def __str__(self):
        return f"{Motorcyle.__str__(self)} with the {self.suspension}"
