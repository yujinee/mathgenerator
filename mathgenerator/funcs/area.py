  
from .__init__ import *


def areaCircle(maxRadius=100):
    r = random.randint(0, maxRadius)
    pi = 22/7
    area = pi*r*r 
    problem = f"Area of circle with radius {r}"
    solution = area
    return problem, solution


areaCircle = Generator("Area", 63, "pi*r*r=", "area", areaCircle)
