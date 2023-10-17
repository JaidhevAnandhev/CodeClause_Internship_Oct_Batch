# Import Libraries
import math


# Addition function
def add(x, y):
    return x + y


# Subtraction function
def sub(x, y):
    return x - y


# Multiplication function
def mul(x, y):
    return x * y


# Division function
def div(x, y):
    return x / y


# Modulus Function
def mod(x, y):
    return x % y


# Power of a number
def power(x, y):
    return x ** y


# Sine function
def sine(x):
    return math.sin(x)


# Cosine function
def cosine(x):
    return math.cos(x)


# Tangent function
def tangent(x):
    return math.tan(x)


# Square root of a number
def square_rt(x):
    return math.sqrt(x)


# Select the choice of the calculator
print("Select the type of the calculator below:")
print("1.NORMAL CALCULATOR")
print("2.SCIENTIFIC CALCULATOR")

calculator_choice = int(input("Enter the choice of the calculator = "))
if calculator_choice == 1:
    cont_arith = 'y'
    while cont_arith.lower() == 'y':

        # Providing multiple mathematical operations
        print("\n~~~NORMAL CALCULATOR~~~")
        print("Enter your choice please!")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("6.Power of a value ")

        nchoice = int(input("Enter a choice = "))
        x = int(input("\nEnter Number 1 = "))
        y = int(input("Enter Number 2 = "))

        if nchoice == 1:
            print("Sum of ", x, "and", y, " = ", add(x, y))

        elif nchoice == 2:
            print("Difference of ", x, "and", y, " = ", sub(x, y))

        elif nchoice == 3:
            print("Product of ", x, "and", y, " = ", mul(x, y))

        elif nchoice == 4:
            print("Division of ", x, "and", y, " = ", div(x, y))

        elif nchoice == 5:
            print("Modulo of ", x, "and", y, " = ", mod(x, y))

        elif nchoice == 6:
            print("Power of ", x, "and", y, " = ", power(x, y))

        else:
            print("Enter a correct number!")

        cont_arith = input("\nContinue ? Y/N = ")
        if cont_arith.lower() == 'n':
            break

else:
    cont_sci = 'y'
    while cont_sci.lower() == 'y':

        # Providing multiple options for scientific calculator
        print("\n~~~SCIENTIFIC CALCULATOR~~~")
        print("Enter your choice please!")
        print("1. Sine ")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Square Root")

        schoice = int(input("Enter a choice = "))
        x = int(input("\nEnter a number = "))

        if schoice == 1:
            print("Sine of ", x, " = ", sine(x))
        elif schoice == 2:
            print("Cosine of ", x, " = ", cosine(x))
        elif schoice == 3:
            print("Tangent of ", x, " = ", tangent(x))
        elif schoice == 4:
            print("Square Root of ", x, " = ", square_rt(x))
        else:
            print("Enter a correct number!")

        cont_sci = input("\nProceed Y/N = ")
        if cont_sci.lower() == 'n':
            break
