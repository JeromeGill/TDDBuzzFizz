import unittest

class FizzBuzzTest(unittest.TestCase):
    """docstring for FizzBuzzTest"""
    def testFizz(self):
        fizzBuzz = FizzBuzz()
        result = fizzBuzz(3)
        self.assertEqual(result,'Fizz')
    def testBuzz(self):
        self.assertEqual(fizzBuzz(20),'Buzz')
    def testFizzBuzz(self):
        self.assertEqual(fizzBuzz(15),'FizzBuzz')