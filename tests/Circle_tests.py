from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Square import Square
from src.Triangle import Triangle
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
                          (-3, 28.27433388230814, 18.84955592153876)])
def test_circle_negative(radius, area, circumference_length):
    with pytest.raises((ValueError)):
        circle = Circle(radius)
        circle.name == f"Circle: radius={radius}"
        circle.get_area == area
        circle.get_perimeter == circumference_length


@pytest.mark.parametrize(("radius", "side_a", "side_b", "base", "result", "result_with_triangle"),
                         [(3, 5, 5, 5, 53.27433388230814, 39.099651429613616)])
def test_add_area(radius, side_a, side_b, base, result, result_with_triangle):
    square = Square(side_a, side_b)
    circle = Circle(radius)
    rectangle = Rectangle(side_a, side_b)
    triangle = Triangle(side_a, side_b, base)
    assert circle.add_area(square) == result
    assert circle.add_area(rectangle) == result
    assert circle.add_area(triangle) == result_with_triangle


@pytest.mark.parametrize(("radius", "side_a", "side_b", "result"),
                         [(0, 5, 5, 100)])
def test_add_area_negative(radius, side_a, side_b, result):
    with pytest.raises(ValueError):
        rectangle = Rectangle(side_a, side_b)
        circle = Circle(radius)
        circle.add_area(rectangle) == result
