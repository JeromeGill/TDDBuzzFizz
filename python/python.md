Python is an object orientated language.

This means we can abstract the complexities of a FizzBuzz solution into two parts, a loop to print the value of fizzbuzz between 1-100 and an abstract FizzBuzz method that it can inherit from a base class. We can set the tests to run purely on the base class without any knowledge of the class with the loop method.

Alternative solutions can be placed in their own class but as the expected result is identical, the same set of unit tests will be perfectly valid. It is just a case of passing each fizzbuzz solution as an argument for the test runner class.

To run the tests 

```$cd /opt/TDDBuzzFizz/python/
    $nosetests FizzBuzzTest.py```

http://www.diveintopython.net/

Initially I tried to write my tests in a FizzBuzzTest.py file. Reading up on how python unit testers work, it turns out the file name should have a test prefix, ie testFizzBuzz. This allows the runner to recognise the file. 

Upon realising that the directory structure of both files in the same place wouldn't scale, I moved FizzBuzz to a src/ directory and testFizzBuzz to a test/ directory.

This introduced the problem of including FizzBuzz as a dependancy for the test class. Python was no longer able to find it. A bit of googling later, I found an __init__.py file adds that directory to pythons path, similar to how adding a .gitignore file enables versioning of an otherwise empty directory.

After some syntatic twiddling I got some failing assertion tests.
```
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
```



 so I began to write a solution. It looked like this,

```
class FizzBuzz:
    """Return Fizz for multiples of 3, 
    Buzz for multiples of 5, 
    FizzBuzz for both"""
    def fizzBuzz(self, a):
        result = ''
        if a % 3 == 0:
            result += 'Fizz'
        if a % 5 == 0:
            result += 'Buzz'
        else:
            result = a
        return result
```

Spot the mistake?

Well the test output looked like this...

```
.F..F.
======================================================================
FAIL: testFizz3 (test.testFizzBuzz.FizzBuzzTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/TDDBuzzFizz/python/test/testFizzBuzz.py", line 10, in testFizz3
    self.assertEqual(result,'Fizz')
AssertionError: 3 != 'Fizz'

======================================================================
FAIL: testFizzBuzz603 (test.testFizzBuzz.FizzBuzzTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/TDDBuzzFizz/python/test/testFizzBuzz.py", line 22, in testFizzBuzz603
    self.assertEqual(result,'Fizz')
AssertionError: 3 != 'Fizz'

----------------------------------------------------------------------
Ran 6 tests in 0.005s
```

FizzBuzz worked, Buzz worked and a numeric output worked. What didn't work was Fizz. Pretty weird as FizzBuzz worked. A closer look at the solution above I was able to quickly work out that Fizz would be overwritten by 'a' if it was not a multiple of 5. The problem being that changing to an else if structure would just swap the failing situation. It needed a bit of duplication.

```
def fizzBuzz(self, a):
        result = ''
        if a % 5 == 0 and a % 3 == 0:
            result += 'FizzBuzz'
        elif a % 3 == 0:
            result += 'Fizz'
        elif a % 5 == 0:
            result += 'Buzz'          
        else:
            result = a
        return result
```
