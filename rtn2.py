"""
Write a funtion called min_of_three that takes three numbers and returns the amallest
without using any built in funtion.
"""
def min_of_three(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
    
result = min_of_three(10, 20, 15)
print("The smallest number is:", result)