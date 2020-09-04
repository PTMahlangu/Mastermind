import unittest
import mastermind
from unittest.mock import patch
from io import StringIO


class TestFunctions(unittest.TestCase):

    def test_creat_code(self):
        """  this method test creat_code() function """
        code =mastermind.create_code()
        for y in range(100):
            self.assertEqual(len(code), 4) 
            self.assertEqual(type(code),list)
            for index in code:
                # Test if there is an index appears more than 1
                self.assertEqual(code.count(index),1)
                # Test if index there is an index less than or equal to zero
                self.assertGreater(index,0)
                # Test of there is an index greater than or equal 8
                self.assertLessEqual(index,8)


    def test_check_correctness(self):
        """  this method test check_correctness() function """
        correct = mastermind.check_correctness(4,1)
        self.assertTrue(correct)

        correct = mastermind.check_correctness(3,12)
        self.assertFalse(correct)
    

    @patch("sys.stdin", StringIO("1t3\n1234\n1234"))
    def test_get_answer_input(self):
        """  this method test get_answer() function """
        user_answer = mastermind.get_answer_input()
        
        self.assertTrue("Input 4 digit code: Please enter exactly 4 digits.",user_answer)
        self.assertEqual(type(user_answer), str)
        self.assertEqual(len(user_answer), 4)

    
    @patch("sys.stdin", StringIO("1234\n1234\n1234\n1234\n1234"))
    def test_take_turn(self):
        """  this method test take_turn() function """

        test = mastermind.take_turn([1,2,3,4])
        self.assertEqual(test,(4,0))

        test = mastermind.take_turn([4,3,2,1])
        self.assertEqual(test,(0,4))

        test = mastermind.take_turn([5,2,3,4])
        self.assertEqual(test,(3,0))

        test = mastermind.take_turn([8,7,6,5])
        self.assertEqual(test,(0,0))

        test = mastermind.take_turn([1,3,2,4])
        self.assertEqual(test,(2,2))



