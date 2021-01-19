#Functions only run when called
number1 = int(input("User input: "))
number2 = int(input("User input: "))

def add(num1, num2):
    sumOfNums = num1 + num2
    return sumOfNums

value = add(number1, number2)
print(value)