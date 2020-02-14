#coding = utf-8
import unittest
from common.Driver import Driver

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("执行初始类方法")
        cls.d = Driver()
        cls.driver = cls.d.startUp()

    def setUp(self):
        print("执行初始化方法")
        self.driver.launch_app()

    def tearDown(self):
        print("执行清理方法")
        self.driver.close_app()

    @classmethod
    def tearDownClass(cls):
        print("执行清理类方法")
        cls.driver.quit()