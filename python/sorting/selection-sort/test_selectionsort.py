import unittest
from selectionsort import selectionsort


class TestSelectionsort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selectionsort([9, 5, 6, 7, 3, 2]), [2, 3, 5, 6, 7, 9])


if __name__ == '__main__':
    unittest.main()
