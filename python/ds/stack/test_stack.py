import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    """
    @classmethod
    def setUpClass(self):
        self.stack_obj = Stack()

    @classmethod
    def tearDownClass(self):
        del self.stack_obj
    """

    def setUp(self):
        self.stack_obj = Stack()

    def test_peek(self):
        self.stack_obj.push('siddhartha')
        self.assertEqual('siddhartha', self.stack_obj.peek())

    def test_size(self):
        self.stack_obj.push(1)
        self.stack_obj.push(2)
        self.assertEqual(2, self.stack_obj.size())

    def test_empty(self):
        self.assertEqual(True, self.stack_obj.isEmpty())
        self.stack_obj.push(1)
        self.assertEqual(False, self.stack_obj.isEmpty())


if __name__ == '__main__':
    unittest.main()
