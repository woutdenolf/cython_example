import unittest
from ... import cython_demo

class test_cython_demo(unittest.TestCase):

    def test_hello(self):
        ret = cython_demo.hello()
        self.assertEqual(ret, 42)
    
    def test_addone(self):
        ret = cython_demo.addone(10)
        self.assertEqual(ret, 11)


def test_suite():
    """Test suite including all test suites"""
    testSuite = unittest.TestSuite()
    testSuite.addTest(test_cython_demo("test_hello"))
    testSuite.addTest(test_cython_demo("test_addone"))
    return testSuite
    
if __name__ == '__main__':
    import sys

    mysuite = test_suite()
    runner = unittest.TextTestRunner()
    if not runner.run(mysuite).wasSuccessful():
        sys.exit(1)
