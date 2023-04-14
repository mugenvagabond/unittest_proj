import unittest
from utils import arrs

"""
Все функции покрыты тестами на 100%!
"""

class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([], -1, "test"), "Индекс должен быть неотрицательным числом!")
        self.assertNotEqual(arrs.get([1, 5, 3], -1, "test"), 3)
        self.assertEqual(arrs.get([1, 5, 3], -4, "test"), "Индекс должен быть неотрицательным числом!")
        self.assertNotEqual(arrs.get([1, 3, 5], "1", "test"), 3)
        self.assertEqual(arrs.get([1, "3", 5], "1", "test"), "Индекс должен быть целым числом!")
        self.assertEqual(arrs.get(["tester", "3", 5], 1, "test"), "3")
        self.assertEqual(arrs.get("testing", 1, "test"), "Данные должны быть в формате списка!")
        self.assertEqual(arrs.get(1, 1, "test"), "Данные должны быть в формате списка!")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])
