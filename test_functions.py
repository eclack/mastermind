import mastermind
import unittest
from unittest.mock import patch
from io import StringIO
import sys

class   TestFunctions(unittest.TestCase):    
    def test_create_code(self):
        for i in range(0, 100):
            result = mastermind.create_code()
            self.assertEqual(len(result), 4)
            for number in result:
                self.assertIn(number, range(1, 9))


    def test_check_correctness(self):
        sys.stdout = StringIO()

        self.assertTrue(mastermind.check_correctness(2, 4))
        self.assertFalse(mastermind.check_correctness(12, 2))
        self.assertTrue(mastermind.check_correctness(4, 4))
        self.assertFalse(mastermind.check_correctness(0, 3))
        self.assertTrue(mastermind.check_correctness(6, 4))
        self.assertFalse(mastermind.check_correctness(1, 7))


    @patch("sys.stdin", StringIO("1a2\n4\nabcdef\nabc\na3f\n1234\n5468\n4321"))
    def test_get_answer_input(self):
    
        sys.stdout = StringIO()

        self.assertEqual(mastermind.get_answer_input(), "1234")
        self.assertEqual(mastermind.get_answer_input(), "5468")
        self.assertEqual(mastermind.get_answer_input(), "4321")
        self.assertEqual(sys.stdout.getvalue(), """Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Input 4 digit code: Input 4 digit code: """)


    def test_show_results(self):
        test = [(1), (2)]
        sys.stdout = StringIO()
        mastermind.show_results(test)
        self.assertEqual(sys.stdout.getvalue(),
         "Number of correct digits in correct place:     1\nNumber of correct digits not in correct place: 2\n")

    @patch("sys.stdin", StringIO("1234\n2134\n1263\n3786\n1234"))
    def test_take_turn(self):
        #suppressing the output
        sys.stdout = StringIO()
        self.assertEqual(mastermind.take_turn([1,2,3,4]), (4, 0)) 
        self.assertEqual(mastermind.take_turn([2,1,5,4]), (3, 0))
        self.assertEqual(mastermind.take_turn([1,2,6,3]), (4, 0))
        self.assertEqual(mastermind.take_turn([3,8,7,6]), (2, 2))
        self.assertEqual(mastermind.take_turn([1,2,3,4]), (4, 0))
    
        sys.stdout = sys.__stdout__

    def test_show_instruction(self):
        sys.stdout = StringIO()

        mastermind.show_instructions()
        self.assertEqual(sys.stdout.getvalue(), '4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.\n')

if __name__ == "__main__":
    unittest.main()