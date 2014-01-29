from unittest import TestCase
from src.FizzBuzz import FizzBuzz

class FizzBuzzTest(TestCase):
    """docstring for FizzBuzzTest"""
    def setUp(self):
        self.FizzBuzz = FizzBuzz();
    def testFizz3(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 3)
        self.assertEqual(result,'Fizz')
    def testBuzz5(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 5)
        self.assertEqual(result,'Buzz')
    def testFizzBuzz15(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 15)
        self.assertEqual(result,'FizzBuzz')
    def testFizzBuzz600(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 600)
        self.assertEqual(result,'FizzBuzz')
    def testFizzBuzz603(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 603)
        self.assertEqual(result,'Fizz')
    def testNumericOut(self):
        result = FizzBuzz.fizzBuzz(self.FizzBuzz, 22)
        self.assertEqual(result,22)