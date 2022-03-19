print("Welcome in simply fibonacii founder")
print("Standard fibonacii start for 0 \n This is start from 1")
SelectCalculatorFunction = int(input("Please input searching fibonachi.."))


def fibonaci_of(number):
    if number in {1, 2}:
        return number
    return fibonaci_of(number - 1) + fibonaci_of(number - 2)


print(fibonaci_of(SelectCalculatorFunction))
