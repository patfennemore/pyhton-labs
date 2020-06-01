'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''


class Pilot:
    def __init__(self, name=None, hours=None, height=None):
        self.name = name
        self.hours = hours
        self.height = height

    def __str__(self):
        return f"{self.name} has been flying for {self.hours} hours and is {self.height} tall"
    



class Plane():
    def __init__(self, model=None, speed=None, color=None):
        self.model = model
        self.speed = speed
        self.color = color

    def __str__(self):
        return f"{self.speed} is the speed of the {self.model} and it is a {self.color} color"

    def __add__(self, other):
        return self.speed + other.speed


class Airport:
    def __init__(self, name=None, length=None, code=None):
        self.name = name
        self.length = length
        self.code = code

    def __str__(self):
        return f"{self.name} has a runway length of {self.length} and the IATA code {self.code}"

    def __add__(self, other):
        """Overloading using the + operator"""
        return self.length + other.name


lax = Airport("Los Angeles", 2721, "LAX")
sin = Airport("Singapore", 4000, "SIN")

daz = Pilot("Dayle", 550, "220cm")
ian = Pilot("Ian", 2500, "110cm")

c152 = Plane("C152", 90, "White")
c172 = Plane("C172", 95, "Blue")

c152.color = "grey"
print(c152)


