'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''


class Planet:
    def __init__(self, color, name, system):
        self.name = name
        self.color = color
        self.system = system

    def __str__(self):
        return f"{self.name} is {self.color} and is in the {self.system}"

    def color(self):
        return f"{self.color}"


mars = Planet("red", "Mars", "Solar System")
print(mars)

earth = Planet("blue", "Earth", "Solar System")
print(earth)

earth.color = "green"
print(earth)

