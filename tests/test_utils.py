import unittest
import utils

class  TestCalc(unittest.TestCase):

    def test_Node(self):
        n1 = utils.Node(5, None)
        print(n1)

    def test_Stack(self):
        stack = utils.Stack()
        stack.push('data1')
        print(stack)