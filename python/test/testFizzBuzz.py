from unittest import TestCase
from src.FizzBuzz import FizzBuzz

class FizzBuzzTest(TestCase):
    """docstring for FizzBuzzTest"""
    def setUp(self):
        self.FizzBuzz = FizzBuzz();
    def testFizz(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 3)
        self.assertEqual(result,'Fizz')
    def testBuzz(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 5)
        self.assertEqual(result,'Buzz')
    def testFizzBuzz(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 15)
        self.assertEqual(result,'FizzBuzz')
    def testNumericOut(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 22)
        self.assertEqual(result,22)