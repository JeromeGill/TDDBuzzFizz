Python is an object orientated language.

This means we can abstract the complexities of a FizzBuzz solution into two parts, a loop to print the value of fizzbuzz between 1-100 and an abstract FizzBuzz method that it can inherit from a base class. We can set the tests to run purely on the base class without any knowledge of the class with the loop method.

Alternative solutions can be placed in their own class but as the expected result is identical, the same set of unit tests will be perfectly valid. It is just a case of passing each fizzbuzz solution as an argument for the test runner class.

To run the tests 

```$cd /opt/TDDBuzzFizz/python/
    $python -m unittest FizzBuzzTest```