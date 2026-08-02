"""
Write a function called ractangle_area that takes length and bradth 
as parameters and prints the area.
"""
def rectangle_area(length, breadth):
    area = length * breadth
    print("Area of rectangle:", area)

length = int(input("Enter the number = "))
breadth = int(input("Enter the number = "))
rectangle_area(length,breadth)