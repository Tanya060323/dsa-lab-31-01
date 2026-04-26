import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides
 
 
class TestGetTriangleTypePositive(unittest.TestCase):
 
    # Тест №1: Равносторонний
    def test_equilateral_int(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")
 
    # Тест №2: Равносторонний
    def test_equilateral_int_2(self):
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")
 
    # Тест №3: Равносторонний
    def test_equilateral_float(self):
        self.assertEqual(get_triangle_type(1.5, 1.5, 1.5), "equilateral")
 
    # Тест №4: Равнобедренный 
    def test_isosceles_ab(self):
        self.assertEqual(get_triangle_type(3, 3, 5), "isosceles")
 
    # Тест №5: Равнобедренный
    def test_isosceles_ac(self):
        self.assertEqual(get_triangle_type(3, 5, 3), "isosceles")
 
    # Тест №6: Равнобедренный
    def test_isosceles_bc(self):
        self.assertEqual(get_triangle_type(5, 3, 3), "isosceles")
 
    # Тест №7: Равнобедренный 
    def test_isosceles_float(self):
        self.assertEqual(get_triangle_type(2.5, 2.5, 3), "isosceles")
 
    # Тест №8: Разносторонний
    def test_nonequilateral_right(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
 
    # Тест №9: Разносторонний 
    def test_nonequilateral_int(self):
        self.assertEqual(get_triangle_type(5, 6, 7), "nonequilateral")
 
    # Тест №10: Разносторонний 
    def test_nonequilateral_float(self):
        self.assertEqual(get_triangle_type(1.1, 2.2, 3.0), "nonequilateral")
 
 
class TestGetTriangleTypeNegative(unittest.TestCase):
 
    # Тест №11
    def test_zero_side_a(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 3, 3)
 
    # Тест №12
    def test_zero_side_b(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 0, 3)
 
    # Тест №13
    def test_zero_side_c(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 3, 0)
 
    # Тест №14
    def test_negative_side_a(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 3, 3)
 
    # Тест №15
    def test_negative_side_b(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, -1, 3)
 
    # Тест №16
    def test_negative_side_c(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 3, -1)
 
    # Тест №17
    def test_all_negative(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-5, -5, -5)
 
    # Тест №18
    def test_triangle_inequality_ab_less_c(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 10)
 
    # Тест №19
    def test_triangle_inequality_ac_less_b(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 10, 2)
 
    # Тест №20
    def test_triangle_inequality_bc_less_a(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(10, 1, 2)
 
    # Тест №21
    def test_degenerate_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)
 
 
if __name__ == "__main__":
    unittest.main()