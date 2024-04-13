import math

class BasicScientificCalculator:
    """

    Functions:
    - add(x, y): Adds two numbers x and y.
    - subtract(x, y): Subtracts y from x.
    - multiply(x, y): Multiplies two numbers x and y.
    - divide(x, y): Divides x by y.
    - power(x, y): Raises x to the power of y.
    - square_root(x): Calculates the square root of x.
    - sin(x): Calculates the sine of x (in radians).
    - cos(x): Calculates the cosine of x (in radians).
    - tan(x): Calculates the tangent of x (in radians).
    - Note: these work for both integers and floats

    Made for BRCS Python Demo by Alex Sheng
    """

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return x / y

    @staticmethod
    def power(x, y):
        return x ** y

    @staticmethod
    def square_root(x):
        if x < 0:
            raise ValueError("Square root is not defined for negative numbers.")
        return math.sqrt(x)

    @staticmethod
    def sin(x):
        return math.sin(x)

    @staticmethod
    def cos(x):
        return math.cos(x)

    @staticmethod
    def tan(x):
        return math.tan(x)

# This is where users change the numbers to change the output

# Initializing Calculator
calculator = BasicScientificCalculator()

# Now that we have defined these functions, we can call them and store the results under varaibles
# (e.g., if I wanted to use the 'add' function with values 'x' and 'y' (given that they are integers or floats) defined earlier and store the result under 'result_add' I would write result_add = calculator.add(5, 3)
# Continuing with the example, if I wanted to call and store the 'power' function under 'power_lol' I would write power_lol = calculator.power(x, y) )

result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(10, 4)
result_multiply = calculator.multiply(2, 6)
result_divide = calculator.divide(8, 2)
result_power = calculator.power(2, 3)
result_sqrt = calculator.square_root(25)
result_sin = calculator.sin(math.pi/2)
result_cos = calculator.cos(0)
result_tan = calculator.tan(math.pi/4)

# Printing results to terminal/shell

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
print(f"Power: {result_power}")
print(f"Square Root: {result_sqrt}")
print(f"Sine: {result_sin}")
print(f"Cosine: {result_cos}")
print(f"Tangent: {result_tan}")
