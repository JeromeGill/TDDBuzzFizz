from unittest import TestCase
from src.Factorial import Factorial

class FactorialTest(TestCase):
    """Test Factorial"""
    def setUp(self):
        self.Factorial = Factorial()
    def test5(self):
        result = Factorial.getFactorialFor(self.Factorial, 5)
        self.assertEqual(result, 120)