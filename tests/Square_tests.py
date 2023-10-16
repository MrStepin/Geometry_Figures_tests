from src.Triangle import Triangle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(5, 25, 20)])
def test_square(side, area, perimeter):
    square = Square(side)
    assert square.name == f"Square: side={side}"
    assert square.get_area == area
    assert square.get_perimeter == perimeter


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(0, 0, 0),
                          (-5, 25, 20),
                          (5, 24, 20),
                          (5, 25, 29)])
def test_square_negative(side, area, perimeter):
    with pytest.raises((ValueError, AssertionError)):
        square = Square(side)
        assert square.name == f"Square: side={side}"
        assert square.get_area == area
        assert square.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "base", "side", "result"),
                         [(2, 2, 3, 4, 17.984313483298443)])
def test_add_area(side_a, side_b, base, side, result):
    square = Square(side)
    triangle = Triangle(side_a, side_b, base)
    assert square.add_area(triangle) == result


@pytest.mark.parametrize(("side_a", "side_b", "base", "side", "result"),
                         [(2, 2, 3, 4, 2)])
def test_add_area_negative(side_a, side_b, base, side, result):
    with pytest.raises(AssertionError):
        square = Square(side)
        triangle = Triangle(side_a, side_b, base)
        assert square.add_area(triangle) == result
