import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides
 
# Тест №1: Равносторонний 
def test_equilateral_int():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 9
 
 
# Тест №2: Равносторонний 
def test_equilateral_int_2():
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 15
 
 
# Тест №3: Равносторонний
def test_equilateral_float():
    t = Triangle(1.5, 1.5, 1.5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == pytest.approx(4.5)
 
 
# Тест №4: Равнобедренный 
def test_isosceles_ab():
    t = Triangle(3, 3, 5)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 11
 
 
# Тест №5: Равнобедренный
def test_isosceles_ac():
    t = Triangle(3, 5, 3)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 11
 
 
# Тест №6: Равнобедренный 
def test_isosceles_bc():
    t = Triangle(5, 3, 3)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 11
 
 
# Тест №7: Равнобедренный 
def test_isosceles_float():
    t = Triangle(2.5, 2.5, 3)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == pytest.approx(8.0)
 
 
# Тест №8: Разносторонний 
def test_nonequilateral_right():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12
 
 
# Тест №9: Разносторонний 
def test_nonequilateral_int():
    t = Triangle(5, 6, 7)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 18
 
 
# Тест №10: Разносторонний 
def test_nonequilateral_float():
    t = Triangle(1.1, 2.2, 3.0)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == pytest.approx(6.3)

 
# Тест №11
def test_zero_side_a():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 3, 3)
 
 
# Тест №12
def test_zero_side_b():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 0, 3)
 
 
# Тест №13
def test_zero_side_c():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 3, 0)
 
 
# Тест №14
def test_negative_side_a():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 3, 3)
 
 
# Тест №15
def test_negative_side_b():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, -1, 3)
 
 
# Тест №16
def test_negative_side_c():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 3, -1)
 
 
# Тест №17
def test_all_negative():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-5, -5, -5)
 
 
# Тест №18
def test_triangle_inequality_ab_less_c():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 10)
 
 
# Тест №19
def test_triangle_inequality_ac_less_b():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 10, 2)
 
 
# Тест №20
def test_triangle_inequality_bc_less_a():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(10, 1, 2)
 
 
# Тест №21
def test_degenerate_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)