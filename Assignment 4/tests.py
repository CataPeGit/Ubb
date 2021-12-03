import unittest

from classes import *


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.test_vector = VectorRepository()

    def test_add_data_examples(self):
        self.test_vector.add_4_data_example()

    def test_add_a_vector_to_the_repository(self):
        # add a vector to the repository test
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v5", "y", 1, [1, 5]))
        tested_vector = self.test_vector.get_vector_at_given_index(0)
        self.assertEqual(tested_vector.get_name_id(), "v5")
        self.assertEqual(tested_vector.get_colour(), "y")
        self.assertEqual(tested_vector.get_type(), 1)
        self.assertEqual(tested_vector.get_values(), [1, 5])
        self.assertNotEqual(tested_vector.get_values(), [1])
        self.assertNotEqual(tested_vector.get_values(), [5])
        self.assertIsNotNone(tested_vector.get_name_id())
        self.assertIsNotNone(tested_vector.get_colour())
        self.assertIsNotNone(tested_vector.get_type())
        self.assertIsNotNone(tested_vector.get_values())

    def test_get_vector_at_given_index(self):
        # test updating a vector at a given index
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v5", "y", 1, [1, 5]))
        self.test_vector.update_vector_at_given_index(
            0, "new", "k", 5, [4, 6, 3])
        tested_vector = self.test_vector.get_vector_at_given_index(0)
        self.assertEqual(tested_vector.get_name_id(), "new")
        self.assertEqual(tested_vector.get_colour(), "k")
        self.assertEqual(tested_vector.get_type(), 5)
        self.assertEqual(tested_vector.get_values(), [4, 6, 3])
        self.assertNotEqual(tested_vector.get_values(), [4])
        self.assertNotEqual(tested_vector.get_values(), [6])
        self.assertIsNotNone(tested_vector.get_name_id())
        self.assertIsNotNone(tested_vector.get_colour())
        self.assertIsNotNone(tested_vector.get_type())
        self.assertIsNotNone(tested_vector.get_values())

    def test_update_vector_by_name_id(self):
        # test update a vector identified by name_id
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v5", "y", 1, [1, 5]))
        self.test_vector.update_vector_by_name_id(
            "v5", "new", "k", 5, [4, 6, 3])
        tested_vector = self.test_vector.get_vector_at_given_index(0)
        self.assertEqual(tested_vector.get_name_id(), "new")
        self.assertEqual(tested_vector.get_colour(), "k")
        self.assertEqual(tested_vector.get_type(), 5)
        self.assertEqual(tested_vector.get_values(), [4, 6, 3])
        self.assertNotEqual(tested_vector.get_values(), [4])
        self.assertNotEqual(tested_vector.get_values(), [6])
        self.assertIsNotNone(tested_vector.get_name_id())
        self.assertIsNotNone(tested_vector.get_colour())
        self.assertIsNotNone(tested_vector.get_type())
        self.assertIsNotNone(tested_vector.get_values())

    def test_delete_vector_at_index(self):
        # testing delete vector at index
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v1", "y", 1, [7]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v2", "g", 2, [1]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v3", "b", 3, [5, 5]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v4", "m", 6, [4, 8]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v5", "k", 2, [1, 8, 4]))

        self.test_vector.delete_vector_at_index(4)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 4)
        self.test_vector.delete_vector_at_index(3)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 3)
        self.test_vector.delete_vector_at_index(2)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 2)
        self.test_vector.delete_vector_at_index(1)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 1)
        self.test_vector.delete_vector_at_index(0)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 0)

        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v6", "r", 1, [1, 5]))

        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v7", "b", 3, [9, 6, 8]))
        self.test_vector.delete_vector_at_index(0)
        tested_vector = self.test_vector.get_vector_at_given_index(0)
        self.assertEqual(tested_vector.get_name_id(), "v7")
        self.assertEqual(tested_vector.get_colour(), "b")
        self.assertEqual(tested_vector.get_type(), 3)
        self.assertEqual(tested_vector.get_values(), [9, 6, 8])

    def test_delete_vector_by_name(self):
        # testing delete vector by name_id
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v1", "y", 1, [7]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v2", "g", 2, [1]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v3", "b", 3, [5, 5]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v4", "m", 6, [4, 8]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v5", "k", 2, [1, 8, 4]))

        self.test_vector.delete_vector_by_name("v4")
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 4)
        self.test_vector.delete_vector_by_name("v2")
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 3)
        self.test_vector.delete_vector_by_name("v3")
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 4)
        self.test_vector.delete_vector_by_name("v1")
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 4)
        self.test_vector.delete_vector_by_name("v5")
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 4)

        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v6", "r", 1, [1, 5]))

        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v7", "b", 3, [9, 6, 8]))
        self.test_vector.delete_vector_by_name("v6")
        tested_vector = self.test_vector.get_vector_at_given_index(0)
        self.assertEqual(tested_vector.get_name_id(), "v7")
        self.assertEqual(tested_vector.get_colour(), "b")
        self.assertEqual(tested_vector.get_type(), 3)
        self.assertEqual(tested_vector.get_values(), [9, 6, 8])

    def test_delete_vectors_between(self):
        # test deleting all vectors that are between two given indexes
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v1", "y", 1, [7]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v2", "g", 2, [1]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v3", "b", 3, [5, 5]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v4", "m", 6, [4, 8]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v5", "k", 2, [1, 8, 4]))

        self.test_vector.delete_vectors_between(3, 5)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 4)
        self.test_vector.delete_vectors_between(2, 4)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 3)
        self.test_vector.delete_vectors_between(1, 3)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 2)
        self.test_vector.delete_vectors_between(0, 2)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 1)
        self.test_vector.delete_vectors_between(-1, 1)
        self.assertRaises(
            IndexError, self.test_vector.delete_vector_at_index, 0)

        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v6", "r", 1, [1, 5]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v7", "b", 3, [9, 6, 8]))
        self.test_vector.delete_vectors_between(-1, 1)
        tested_vector = self.test_vector.get_vector_at_given_index(0)
        self.assertEqual(tested_vector.get_name_id(), "v7")
        self.assertEqual(tested_vector.get_colour(), "b")
        self.assertEqual(tested_vector.get_type(), 3)
        self.assertEqual(tested_vector.get_values(), [9, 6, 8])

    def test_update_color_by_name_id(self):
        # test updating the color of a vector identified by name_id
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v1", "y", 1, [7]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v2", "g", 2, [1]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v3", "b", 3, [5, 5]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v4", "m", 6, [4, 8]))
        self.test_vector.add_a_vector_to_the_repository(
            MyVector("v5", "k", 2, [1, 8, 4]))

        tested_vector = self.test_vector.get_vector_at_given_index(0)
        self.test_vector.update_color_by_name_id("v1", "r")
        self.assertEqual(tested_vector.get_colour(), "r")
        self.assertNotEqual(tested_vector.get_colour(), "y")

        tested_vector = self.test_vector.get_vector_at_given_index(1)
        self.test_vector.update_color_by_name_id("v2", "b")
        self.assertEqual(tested_vector.get_colour(), "b")
        self.assertNotEqual(tested_vector.get_colour(), "r")

        tested_vector = self.test_vector.get_vector_at_given_index(2)
        self.test_vector.update_color_by_name_id("v3", "g")
        self.assertEqual(tested_vector.get_colour(), "g")
        self.assertNotEqual(tested_vector.get_colour(), "b")

        tested_vector = self.test_vector.get_vector_at_given_index(3)
        self.test_vector.update_color_by_name_id("v4", "b")
        self.assertEqual(tested_vector.get_colour(), "b")
        self.assertNotEqual(tested_vector.get_colour(), "m")

        tested_vector = self.test_vector.get_vector_at_given_index(4)
        self.test_vector.update_color_by_name_id("v5", "m")
        self.assertEqual(tested_vector.get_colour(), "m")
        self.assertNotEqual(tested_vector.get_colour(), "k")
