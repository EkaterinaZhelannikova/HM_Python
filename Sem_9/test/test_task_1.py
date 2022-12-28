import sys
import os
import unittest
from task_1 import sum_num
sys.path.append(os.path.join(os.getcwd(), 'task_1.py'))


class TestSumNum(unittest.TestCase):
    def test_sum_num(self):
        self.assertEqual(sum_num(3), 369)

    def test_sum_num_not(self):
        self.assertNotEqual(sum_num(3), 100)


if __name__ == '__main__':
    unittest.main()
