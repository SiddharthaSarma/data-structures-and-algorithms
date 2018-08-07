import unittest
from insertionsort import insertionsort


class TestInsertionsort(unittest.TestCase):
    def test_insertionsort(self):
        self.assertEqual(insertionsort([1, 7, 5, 8, 2, 3, 4]), [1, 2, 3, 4, 5, 7, 8])


if __name__ == '__main__':
    unittest.main()
