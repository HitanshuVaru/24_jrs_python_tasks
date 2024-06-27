import math

user_input = input("Enter a number: ")

if user_input.isalpha() or '-' in user_input:
    print("Not a valid input")
else:
    if user_input.isdigit():
        number = int(user_input)
        if number < 0:
            print("Please enter a non-negative integer")
        else:
            factorial = math.factorial(number)
            print("The factorial of " + str(number) + " is " + str(factorial))
    else:
        print("Not a valid input")
