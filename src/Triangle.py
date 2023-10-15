from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, base):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or base <= 0:
            raise ValueError("Can't create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.base = base
        self.name = f"Triangle: side_a={side_a}, side_b={side_b}, base={base}"

    @property
    def get_perimeter(self):
        perimeter = float(self.side_a + self.side_b + self.base)
        return perimeter

    @property
    def get_area(self):
        p = self.get_perimeter / 2.0
        h = (2 * (math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.base)))) / self.base
        s = float((self.base * h) / 2)
        return s

