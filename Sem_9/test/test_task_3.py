import sys
import os
import unittest
from task_3 import my_list
sys.path.append(os.path.join(os.getcwd(), 'task_3.py'))


class TestMyList(unittest.TestCase):
    def test_my_list(self):
        a = my_list(1, 2, 3)
        b = 1
        self.assertIn(b, a)

    def test_my_list_not(self):
        a = my_list(1, 2, 3)
        b = 4
        self.assertNotIn(b, a)


if __name__ == '__main__':
    unittest.main()
