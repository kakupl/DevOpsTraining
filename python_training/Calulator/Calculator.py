print("Welcome in simply calculator")
print("What do you wont to do ?"
      "\n 1. Sum numbers"
      "\n 2. Subtracts numbers"
      "\n 3. Multiply numbers"
      "\n 4. Divide numbers")
print("Please select from 1 to 4")

SelectCalculatorFunction = int(input("Please select function.."))
if SelectCalculatorFunction == str():
    print("You add a string value, we expect a integer value")
    exit()
elif SelectCalculatorFunction > 4:
    print("You choose value which is not supported")
    exit()

GetFirstValue = int(input("Add first value.."))
GetSecondValue = int(input("Add second value.."))


class Calculator:
    def __init__(self):
        pass

    def sum_add(x, y):
        count = x + y
        return count

    def subtracts_add(x, y):
        substract = x - y
        return substract

    def multiply_add(x, y):
        multiply = x * y
        return multiply

    def divide_add(x, y):
        if y != 0:
            divide = x / y
            return int(divide)


if SelectCalculatorFunction == 1:
    print("You selected sum of numbers")
    calculator = Calculator
    print("Sum: ", calculator.sum_add(GetFirstValue, GetSecondValue))
elif SelectCalculatorFunction == 2:
    print("You selected subtracts of numbers")
    calculator = Calculator
    print("Subtracts", calculator.subtracts_add(GetFirstValue, GetSecondValue))
elif SelectCalculatorFunction == 3:
    print("You selected multiply of numbers")
    calculator = Calculator
    print("Multiply", calculator.multiply_add(GetFirstValue, GetSecondValue))
elif SelectCalculatorFunction == 4:
    print("You selected divide of numbers")
    calculator = Calculator
    print("Divide", calculator.divide_add(GetFirstValue, GetSecondValue))
