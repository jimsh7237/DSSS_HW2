import unittest
from math_quiz import generate_integer, random_operator, create_problem

class TestMathGame(unittest.TestCase):

    def test_generate_integer(self):
        """Test that generate_integer returns a value within the specified range."""
        min_value, max_value = 1, 10
        result = generate_integer(min_value, max_value)
        self.assertGreaterEqual(result, min_value, "Result should be >= min_value")
        self.assertLessEqual(result, max_value, "Result should be <= max_value")

    def test_random_operator(self):
        """Test that random_operator returns one of the valid operators."""
        valid_operators = ['+', '-', '*']
        result = random_operator()
        self.assertIn(result, valid_operators, "Result should be one of '+', '-', '*'")

    def test_create_problem(self):
        """Test that create_problem returns the correct problem string and answer."""
        # Test addition
        num1, num2, operator = 3, 4, '+'
        problem, answer = create_problem(num1, num2, operator)
        self.assertEqual(problem, "3 + 4", "Problem string should be formatted correctly")
        self.assertEqual(answer, 7, "Answer should be 7 for 3 + 4")

        # Test subtraction
        num1, num2, operator = 10, 4, '-'
        problem, answer = create_problem(num1, num2, operator)
        self.assertEqual(problem, "10 - 4", "Problem string should be formatted correctly")
        self.assertEqual(answer, 6, "Answer should be 6 for 10 - 4")

        # Test multiplication
        num1, num2, operator = 2, 5, '*'
        problem, answer = create_problem(num1, num2, operator)
        self.assertEqual(problem, "2 * 5", "Problem string should be formatted correctly")
        self.assertEqual(answer, 10, "Answer should be 10 for 2 * 5")

if __name__ == '__main__':
    unittest.main()
