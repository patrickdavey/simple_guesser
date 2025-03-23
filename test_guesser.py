import unittest
from guesser import parse_guess, evaluate_guess

class TestGuesser(unittest.TestCase):

    def test_parse_guess_valid(self):
        self.assertEqual(parse_guess("42"), ("ok", 42))
        self.assertEqual(parse_guess("0"), ("ok", 0))
        self.assertEqual(parse_guess("100"), ("ok", 100))

    def test_parse_guess_out_of_range(self):
        self.assertEqual(parse_guess("-1"), ("out_of_range", None))
        self.assertEqual(parse_guess("101"), ("out_of_range", None))

    def test_parse_guess_invalid(self):
        self.assertEqual(parse_guess("abc"), ("invalid", None))
        self.assertEqual(parse_guess("10.5"), ("invalid", None))
        self.assertEqual(parse_guess(""), ("invalid", None))

    def test_evaluate_guess_low(self):
        self.assertEqual(evaluate_guess(25, 50), "low")

    def test_evaluate_guess_high(self):
        self.assertEqual(evaluate_guess(75, 50), "high")

    def test_evaluate_guess_correct(self):
        self.assertEqual(evaluate_guess(50, 50), "correct")

if __name__ == '__main__':
    unittest.main()

