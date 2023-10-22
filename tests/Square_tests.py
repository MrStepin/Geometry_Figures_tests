from src.Triangle import Triangle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(5, 5, 25, 20)])
def test_square(side_a, side_b, area, perimeter):
    square = Square(side_a, side_b)
    assert square.name == f"Square: side_a={side_a}, side_b={side_b}"
    assert square.get_area == area
    assert square.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(0, 0, 0, 0),
                          (-5, 5, 25, 20)])
def test_square_negative(side_a, side_b, area, perimeter):
    with pytest.raises((ValueError)):
        square = Square(side_a, side_b)
        square.name == f"Square: side_a={side_a}, side_b={side_b}"
        square.get_area == area
        square.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "base", "side_c", "side_d", "result"),
                         [(4, 4, 3, 2, 2, 17.984313483298443)])
def test_add_area(side_a, side_b, base, side_c, side_d, result):
    square = Square(side_a, side_b)
    triangle = Triangle(side_c, side_d, base)
    assert square.add_area(triangle) == result


@pytest.mark.parametrize(("side_a", "side_b", "base", "side_c", "side_d", "result"),
                         [("4", 4, 3, 2, 2, 2)])
def test_add_area_negative(side_a, side_b, base, side_c, side_d, result):
    with pytest.raises(TypeError):
        square = Square(side_a, side_b)
        triangle = Triangle(side_c, side_d, base)
        square.add_area(triangle) == result
