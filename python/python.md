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