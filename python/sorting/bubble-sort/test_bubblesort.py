import unittest
from bubblesort import bubblesort


class TestBubblesort(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubblesort([1, 6, 5, 4, 3]), [1, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
