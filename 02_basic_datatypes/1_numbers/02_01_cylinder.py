'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

import math

radius = 3.14

height = 5

volume_cylinder = math.pi*radius**2*height
print(volume_cylinder)

surface_area_cylinder = (2*math.pi*radius*height) + (2*math.pi*radius**2)
print(surface_area_cylinder)