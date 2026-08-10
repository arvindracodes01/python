class NegativeNumberError(Exception):
    pass


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a < 0 or b < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

    result = a / b

except ValueError:
    print("Please enter valid numbers!")

except ZeroDivisionError:
    print("Second number cannot be zero!")

except NegativeNumberError as e:
    print("Error:", e)

else:
    print("Division successful!")
    print("Result =", result)

finally:
    print("Program execution completed.")