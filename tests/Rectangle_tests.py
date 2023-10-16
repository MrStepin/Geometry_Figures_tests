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
                          (-5, 10, 50, 30),
                          (2, 8, -16, -20)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises((ValueError, AssertionError)):
        rectangle = Rectangle(side_a, side_b)
        assert rectangle.name == f"Rectangle: side_a={side_a}, side_b={side_b}"
        assert rectangle.get_area == area
        assert rectangle.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side", "result"),
                         [(10, 15, 5, 175)])
def test_add_area(side_a, side_b, side, result):
    square = Square(side)
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.add_area(square) == result


@pytest.mark.parametrize(("side_a", "side_b", "radius", "result"),
                         [(2, 5, 5, 15)])
def test_add_area_negative(side_a, side_b, radius, result):
    with pytest.raises(AssertionError):
        rectangle = Rectangle(side_a, side_b)
        circle = Circle(radius)
        assert circle.add_area(rectangle) == result
