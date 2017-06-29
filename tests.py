import unittest

from errors import ApplicationError
from generator import Generator
from math_utils import dot_product


class TestGenerator(unittest.TestCase):
    def test_empty(self):
        generator = Generator([])()
        all_items = yield from generator
        self.assertEqual([], all_items)

    def test_one_piece(self):
        generator = Generator([5, 3])()
        all_items = yield from generator
        self.assertEqual([5, 5, 5], all_items)

    def test_two_pieces(self):
        generator = Generator([5, 3, 4, 2])()
        all_items = yield from generator
        self.assertEqual([5, 5, 5, 4, 4], all_items)

    def test_even_number_of_items(self):
        with self.assertRaises(ValueError):
            Generator([5, 3, 4])()

    def test_vector_length(self):
        generator = Generator([5, 3, 4, 2])
        self.assertEqual(5, generator.vector_length)

    def test_zero_vector_length(self):
        generator = Generator([])
        self.assertEqual(0, generator.vector_length)


class TestDotProduct(unittest.TestCase):
    def test_ok_input(self):
        first = [2, 2]
        second = [3, 2]
        result = dot_product(first, second)
        self.assertEqual(12, result)

    def test_unequal_vectors(self):
        first = [2, 2]
        second = [3, 3]
        with self.assertRaises(ApplicationError):
            dot_product(first, second)
