import unittest

from math_utils import vector_utils
from math_utils.errors import ApplicationError
from math_utils.vector_unpacker import VectorUnpacker


class TestUnpacker(unittest.TestCase):
    def test_empty(self):
        unpacker = VectorUnpacker([])()
        all_items = yield from unpacker
        self.assertEqual([], all_items)

    def test_one_piece(self):
        unpacker = VectorUnpacker([5, 3])()
        all_items = yield from unpacker
        self.assertEqual([5, 5, 5], all_items)

    def test_two_pieces(self):
        unpacker = VectorUnpacker([5, 3, 4, 2])()
        all_items = yield from unpacker
        self.assertEqual([5, 5, 5, 4, 4], all_items)

    def test_even_number_of_items(self):
        with self.assertRaises(ValueError):
            VectorUnpacker([5, 3, 4])()

    def test_vector_length(self):
        unpacker = VectorUnpacker([5, 3, 4, 2])
        self.assertEqual(5, unpacker.unpacked_vector_length)

    def test_zero_vector_length(self):
        unpacker = VectorUnpacker([])
        self.assertEqual(0, unpacker.unpacked_vector_length)


class TestDotProduct(unittest.TestCase):
    def test_ok_input(self):
        first = [2, 2]
        second = [3, 2]
        result = vector_utils.dot_product(first, second)
        self.assertEqual(12, result)

    def test_ok_input_multiple_pieces(self):
        first = [2, 2, 6, 1, 8, 1, 3, 1]
        second = [3, 2, 4, 3]
        result = vector_utils.dot_product(first, second)
        self.assertEqual(80, result)

    def test_unequal_vectors(self):
        first = [2, 2]
        second = [3, 3]
        with self.assertRaises(ApplicationError):
            vector_utils.dot_product(first, second)
