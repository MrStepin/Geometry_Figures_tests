from src.Triangle import Triangle
from src.Circle import Circle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "base", "area", "perimeter"),
                         [(2, 2, 3, 1.984313483298443, 7)])
def test_triangle(side_a, side_b, base, area, perimeter):
    triangle = Triangle(side_a, side_b, base)
    assert triangle.name == f"Triangle: side_a={side_a}, side_b={side_b}, base={base}"
    assert triangle.get_area == area
    assert triangle.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "base", "area", "perimeter"),
                         [(0, 0, 0, 0, 0),
                          (-2, 2, 3, 1.984313483298443, 7),
                          (2, 4, 16, 20, 10)])
def test_triangle_negative(side_a, side_b, base, area, perimeter):
    with pytest.raises((ValueError, AssertionError)):
        triangle = Triangle(side_a, side_b, base)
        triangle.name == f"Triangle: side_a={side_a}, side_b={side_b}, base={base}"
        triangle.get_area == area
        triangle.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "base", "side_c", "side_d", "result"),
                         [(2, 2, 3, 5, 5, 26.984313483298443)])
def test_add_area(side_a, side_b, base, side_c, side_d, result):
    square = Square(side_c, side_d)
    triangle = Triangle(side_a, side_b, base)
    assert triangle.add_area(square) == result


@pytest.mark.parametrize(("side_a", "side_b", "base", "radius", "result"),
                         [(2, 0, 3, 5, 15)])
def test_add_area_negative(side_a, side_b, base, radius, result):
    with pytest.raises(ValueError):
        triangle = Triangle(side_a, side_b, base)
        circle = Circle(radius)
        circle.add_area(triangle) == result
