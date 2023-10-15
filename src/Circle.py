from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can't create Circle")
        self.radius = radius
        self.name = f"Circle: radius={radius}"

    @property
    def get_perimeter(self):
        circumference_length = 2*math.pi*self.radius
        return float(circumference_length)

    @property
    def get_area(self):
        s = math.pi*(self.radius**2)
        return float(s)

