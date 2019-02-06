import unittest
from demo_class import MyClass
import sys

class MyClassTestCase(unittest.TestCase):
    """
    Test for demo_class.py
    """
    def testcase_1(self):
        test_obj = MyClass(10, 'a')
        res = test_obj.tasks()
        print('started testcase1')
        self.assertEquals(res, '10a')

    def testcase_2(self):
        test_obj = MyClass(10, 'a')
        res = test_obj.tasks()
        print('started testcase1')
        self.assertEquals(res, -99)

    def testcase_3(self):
        test_obj = MyClass(10, 20)
        res = test_obj.tasks()
        print('started testcase1')
        self.assertEquals(res, -99)

    def testcase_4(self):
        test_obj = MyClass(10,20)
        res = test_obj.tasks()
        print('started testcase1')
        self.assertEquals(res, 30)


if __name__ == "__main__":
    unittest.main()


