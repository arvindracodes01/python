"""
Write a function called find_max that takes three numbers as parameters 
and prints the largest one.
"""
def find_max(a, b, c):
    if a > b and a > c:
        print("The largest number is:", a)
    elif b > a and b > c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)


find_max(10, 20, 15)