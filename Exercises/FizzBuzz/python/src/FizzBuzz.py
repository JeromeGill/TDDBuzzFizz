class FizzBuzz:
    """Return Fizz for multiples of 3, 
    Buzz for multiples of 5, 
    FizzBuzz for both"""
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