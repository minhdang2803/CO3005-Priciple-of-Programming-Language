import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """Class a{} Class a{}"""
        expect = "Redeclared Class:a"
        self.assertTrue(TestCodeGen.test(input,expect,1))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],VoidType(),Block([],[
    # 			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
