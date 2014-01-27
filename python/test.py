import unittest
import fizzBuzz

class FizzBuzzTest(unittest.TestCase):
    """docstring for FizzBuzzTest"""
    def runTest(self):
        assert fizzBuzz(15) == 'FizzBuzz', '15 does not return Fizzbuzz'
        assert fizzBuzz(3) == 'Fizz', '3 does not return Fizz'
        assert fizzBuzz(20) == 'Buzz', '20 does not return Buzz'
        assert fizzBuzz(26) == '26', '26 does not return its numeric value'