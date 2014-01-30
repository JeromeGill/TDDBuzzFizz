class Factorial():
    
    """A Factorial the product of all the positive integers less than or equal to n
    i.e for 5 it is 5x4x3x2x1"""
	
    def getFactorialFor(self, value):
		result = value;
		for i in range(1, value):
			result *= i;
		return result;
