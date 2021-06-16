# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
# the value of squared a divided by b, construct a try-except block which raises an exception if the two values given by
# the input function were not numbers, and if value b was zero (cannot divide by zero).


def math_func(a, b):
    result = int(a)*int(a)/int(b)
    return result


num1 = input('Type in the first number: ')
num2 = input('Type in the second number: ')
try:
    print(f'Result: {math_func(num1, num2)}')
except ValueError:
    print('Wrong input! Digital data is only available')
except ZeroDivisionError:
    print('Error! Division by zero...')
