from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a, side_b):
        Rectangle.__init__(self, side_a, side_b)
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Can't create Square")
        self.side_a = side_a
        self.side_b = side_b
        self.name = f"Square: side_a={side_a}, side_b={side_b}"



