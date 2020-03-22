import unittest
from Sudoku import judge

class test_judge(unittest.TestCase):
    def test_myfun(self):
        test_num = judge(0, 1, 2)#测试数值
        self.assertEqual(test_num, 1)#期望值


if __name__ == '__main__':
    unittest.main()
