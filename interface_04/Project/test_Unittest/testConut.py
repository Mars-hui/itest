#coding=utf-8

from test_Unittest import Count
import unittest

class TestCount(unittest.TestCase):

    c = Count.Count()
    @classmethod
    def setUpClass(cls):
        print("\n这是所有测试用例前的准备工作")

    @classmethod
    def tearDownClass(cls):
        print("\n这是所有测试用例后的清理工作")

    def setUp(self):
        print("\n这是一个测试用例前的准备工作")

    def tearDown(self):
        print("\n这是一个测试用例后的清理工作")

    # @unittest.skip("临时跳过测试用例")
    def test_add(self):
        res1 = self.c.add(1,2)
        res2 = self.c.add(2, 2)
        print(res1,res2)
        self.assertEqual(3, int(res1))
        self.assertEqual(4, int(res2))
        print("add,OK!")

    def test_jian(self):
        res1 = self.c.jian(3,2)
        res2 = self.c.jian(2, 2)
        self.assertEqual(1,int(res1))
        self.assertEqual(0,int(res2))
        print("jian,OK!")

    def test_cheng(self):
        res1 = self.c.cheng(3,2)
        res2 = self.c.cheng(2, 2)
        self.assertEqual(6,int(res1))
        self.assertEqual(4,int(res2))
        print("cheng,OK!")

    def test_chu(self):
        res1 = self.c.chu(3,2)
        res2 = self.c.chu(2, 2)
        self.assertEqual(1,int(res1))
        self.assertEqual(1,int(res2))
        print("chu,OK!")

# if __name__ == '__main__':
#     # unittest.main(verbosity=3)
#     suite = unittest.TestSuite()
#     suite.addTest(TestCount("test_add"))
#
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)
