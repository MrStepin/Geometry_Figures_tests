from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        if side <= 0:
            raise ValueError("Can't create Square")
        self.side = side
        self.name = f"Square: side={side}"

    @property
    def get_perimeter(self):
        perimeter = 4 * self.side
        return float(perimeter)

    @property
    def get_area(self):
        s = self.side ** 2
        return float(s)


