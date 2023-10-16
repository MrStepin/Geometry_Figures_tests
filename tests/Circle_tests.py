from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("radius", "area", "circumference_length"),
                         [(3, 28.274333882308138, 18.84955592153876)])
def test_circle(radius, area, circumference_length):
    circle = Circle(radius)
    assert circle.name == f"Circle: radius={radius}"
    assert circle.get_area == area
    assert circle.get_perimeter == circumference_length


@pytest.mark.parametrize(("radius", "area", "circumference_length"),
                         [(0, 0, 0),
                          (-3, 28.27433388230814, 18.84955592153876),
                          (5, 8, 16)])
def test_circle_negative(radius, area, circumference_length):
    with pytest.raises((ValueError, AssertionError)):
        circle = Circle(radius)
        assert circle.name == f"Circle: radius={radius}"
        assert circle.get_area == area
        assert circle.get_perimeter == circumference_length


@pytest.mark.parametrize(("radius", "side", "result"),
                         [(3, 5, 53.27433388230814)])
def test_add_area(radius, side, result):
    square = Square(side)
    circle = Circle(radius)
    assert circle.add_area(square) == result


@pytest.mark.parametrize(("radius", "side_a", "side_b", "result"),
                         [(3, 5, 5, 53.2743338823081)])
def test_add_area_negative(radius, side_a, side_b, result):
    with pytest.raises(AssertionError):
        rectangle = Rectangle(side_a, side_b)
        circle = Circle(radius)
        assert circle.add_area(rectangle) == result
