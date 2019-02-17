import unittest
from ... import wrap_demo

class test_wrap_demo(unittest.TestCase):

    def test_hello(self):
        ret = wrap_demo.hello()
        self.assertEqual(ret, 42)
    
    def test_echo(self):
        ret = wrap_demo.echo(10)
        self.assertEqual(ret, 11)


def test_suite():
    """Test suite including all test suites"""
    testSuite = unittest.TestSuite()
    testSuite.addTest(test_wrap_demo("test_hello"))
    testSuite.addTest(test_wrap_demo("test_echo"))
    return testSuite
    
if __name__ == '__main__':
    import sys

    mysuite = test_suite()
    runner = unittest.TextTestRunner()
    if not runner.run(mysuite).wasSuccessful():
        sys.exit(1)
