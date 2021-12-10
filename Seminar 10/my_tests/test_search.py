import unittest
from utils.search import *
from utils import criterions


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.unordered = [1, 3, 6, 2, 9, 0, 2, 15]
        self.ordered = sorted(self.unordered)

    def test_sequential_search_unordered(self):
        self.assertEqual(sequential_search_unordered(self.unordered, 2), 6)
        self.assertEqual(sequential_search_unordered(self.unordered, 4), -1)
        self.assertEqual(sequential_search_unordered(self.unordered, 9), 4)

    def test_sequential_search_ordered(self):
        self.assertEqual(sequential_search_ordered(self.ordered, 2), 2)
        self.assertEqual(sequential_search_ordered(self.ordered, 4), -1)
        self.assertEqual(sequential_search_ordered(self.ordered, 9), 6)

    def test_binary_search(self):
        self.assertEqual(binary_search(self.ordered, 3), 4)
        self.assertEqual(binary_search(self.ordered, 4), -1)
        self.assertEqual(binary_search(self.ordered, 9), 6)

    def test_in_built_filter(self):
        self.assertEqual(in_built_filter(self.unordered, criterions.is_even), [6, 2, 0, 2])
        self.assertEqual(in_built_filter(self.ordered, criterions.is_even), [0, 2, 2, 6])
        self.assertEqual(in_built_filter(self.unordered, criterions.is_armstrong), [1, 0])
        self.assertEqual(in_built_filter(self.ordered, criterions.is_armstrong), [0, 1])
        self.assertEqual(in_built_filter(self.unordered, criterions.criterion_i_2), [0])
        self.assertEqual(in_built_filter(self.ordered, criterions.criterion_i_2), [0])
        self.assertEqual(in_built_filter(self.unordered, criterions.criterion_i_3), [1, 3, 6, 2, 9, 0, 2])
        self.assertEqual(in_built_filter(self.ordered, criterions.criterion_i_3), [0, 1, 2, 2, 3, 6, 9])

    def test_my_filter(self):
        self.assertEqual(my_filter(self.unordered, criterions.is_even), [6, 2, 0, 2])
        self.assertEqual(my_filter(self.ordered, criterions.is_even), [0, 2, 2, 6])
        self.assertEqual(my_filter(self.unordered, criterions.is_armstrong), [1, 0])
        self.assertEqual(my_filter(self.ordered, criterions.is_armstrong), [0, 1])
        self.assertEqual(my_filter(self.unordered, criterions.criterion_i_2), [0])
        self.assertEqual(my_filter(self.ordered, criterions.criterion_i_2), [0])
        self.assertEqual(my_filter(self.unordered, criterions.criterion_i_3), [1, 3, 6, 2, 9, 0, 2])
        self.assertEqual(my_filter(self.ordered, criterions.criterion_i_3), [0, 1, 2, 2, 3, 6, 9])
