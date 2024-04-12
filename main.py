import math

class BasicScientificCalculator:
    """
    Class representing a basic scientific calculator.

    Methods:
    - add(x, y): Adds two numbers x and y.
    - subtract(x, y): Subtracts y from x.
    - multiply(x, y): Multiplies two numbers x and y.
    - divide(x, y): Divides x by y.
    - power(x, y): Raises x to the power of y.
    - square_root(x): Calculates the square root of x.
    - sin(x): Calculates the sine of x (in radians).
    - cos(x): Calculates the cosine of x (in radians).
    - tan(x): Calculates the tangent of x (in radians).
    """

    @staticmethod
    def add(x, y):
        """
        Adds two numbers x and y.

        Parameters:
        - x: int or float
            The first number.
        - y: int or float
            The second number.

        Returns:
        - int or float:
            The sum of x and y.
        """
        return x + y

    @staticmethod
    def subtract(x, y):
        """
        Subtracts y from x.

        Parameters:
        - x: int or float
            The number to be subtracted from.
        - y: int or float
            The number to subtract.

        Returns:
        - int or float:
            The result of x - y.
        """
        return x - y

    @staticmethod
    def multiply(x, y):
        """
        Multiplies two numbers x and y.

        Parameters:
        - x: int or float
            The first number.
        - y: int or float
            The second number.

        Returns:
        - int or float:
            The product of x and y.
        """
        return x * y

    @staticmethod
    def divide(x, y):
        """
        Divides x by y.

        Parameters:
        - x: int or float
            The dividend.
        - y: int or float
            The divisor (should not be zero).

        Returns:
        - float:
            The result of x divided by y.
        
        Raises:
        - ZeroDivisionError:
            If y is zero, division by zero is not allowed.
        """
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return x / y

    @staticmethod
    def power(x, y):
        """
        Raises x to the power of y.

        Parameters:
        - x: int or float
            The base number.
        - y: int or float
            The exponent.

        Returns:
        - float:
            The result of x raised to the power of y.
        """
        return x ** y

    @staticmethod
    def square_root(x):
        """
        Calculates the square root of x.

        Parameters:
        - x: int or float
            The number to find the square root of (should be non-negative).

        Returns:
        - float:
            The square root of x.
        
        Raises:
        - ValueError:
            If x is negative, square root is not defined for negative numbers.
        """
        if x < 0:
            raise ValueError("Square root is not defined for negative numbers.")
        return math.sqrt(x)

    @staticmethod
    def sin(x):
        """
        Calculates the sine of x (in radians).

        Parameters:
        - x: int or float
            The angle in radians.

        Returns:
        - float:
            The sine of x.
        """
        return math.sin(x)

    @staticmethod
    def cos(x):
        """
        Calculates the cosine of x (in radians).

        Parameters:
        - x: int or float
            The angle in radians.

        Returns:
        - float:
            The cosine of x.
        """
        return math.cos(x)

    @staticmethod
    def tan(x):
        """
        Calculates the tangent of x (in radians).

        Parameters:
        - x: int or float
            The angle in radians.

        Returns:
        - float:
            The tangent of x.
        """
        return math.tan(x)

# Example of using the BasicScientificCalculator class:

# Initializing the calculator
calculator = BasicScientificCalculator()

# Performing calculations
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(10, 4)
result_multiply = calculator.multiply(2, 6)
result_divide = calculator.divide(8, 2)
result_power = calculator.power(2, 3)
result_sqrt = calculator.square_root(25)
result_sin = calculator.sin(math.pi/2)
result_cos = calculator.cos(0)
result_tan = calculator.tan(math.pi/4)

# Displaying the results
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
print(f"Power: {result_power}")
print(f"Square Root: {result_sqrt}")
print(f"Sine: {result_sin}")
print(f"Cosine: {result_cos}")
print(f"Tangent: {result_tan}")
