from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(3, 7, 21, 20)])
def test_rectangle(side_a, side_b, area, perimeter):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.name == f"Rectangle: side_a={side_a}, side_b={side_b}"
    assert rectangle.get_area == area
    assert rectangle.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(0, 0, 0, 0),
                          (-5, 10, 50, 30)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises((ValueError)):
        rectangle = Rectangle(side_a, side_b)
        rectangle.name == f"Rectangle: side_a={side_a}, side_b={side_b}"
        rectangle.get_area == area
        rectangle.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "result"),
                         [(10, 15, 5, 5, 175)])
def test_add_area(side_a, side_b, side_c, side_d, result):
    square = Square(side_c, side_d)
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.add_area(square) == result


@pytest.mark.parametrize(("side_a", "side_b", "radius", "result"),
                         [(10, -15, 0, 175)])
def test_add_area_negative(side_a, side_b, radius, result):
    with pytest.raises(ValueError):
        rectangle = Rectangle(side_a, side_b)
        circle = Circle(radius)
        circle.add_area(rectangle) == result
