import sys
import os
import unittest
from task_2 import my_func
sys.path.append(os.path.join(os.getcwd(), 'task_2.py'))


class TestMyFunc(unittest.TestCase):
    def test_my_func(self):
        self.assertTrue(my_func())

    def test_my_func_not(self):
        a = [0, 1, 2, 3, 4, 5]
        b = [i for i in range(6)]
        self.assertNotIn(a, b)


if __name__ == '__main__':
    unittest.main()
