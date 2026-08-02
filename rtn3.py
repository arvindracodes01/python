"""
Write a function called absolute value that takes a number and returns its absolute value
 without using the built in abs funtion
 """
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return num * -1

print(absolute_value(-10))
print(absolute_value(9))
print(absolute_value(4))
