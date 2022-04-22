import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_233(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a::$b=2;
            a::$e();
            a::$c::$d=2;
        } 
    }
    """
        expect = "Error on line 6 col 17: ::"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a::$b=2;
            a::$e();
            a::$c()::$d=2;
        } 
    }
    """
        expect = "Error on line 6 col 19: ::"
        self.assertTrue(TestParser.test(input, expect, 234))