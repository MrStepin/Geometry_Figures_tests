




@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16),
                          (5, 25, 20)])
def test_sq(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == f"Square {side_a}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter