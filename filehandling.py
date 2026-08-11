# Python File Handling - Practice


# 1. Writing data to a file
with open("marks.txt", "w") as file:
    file.write("45\n")
    file.write("78\n")
    file.write("92\n")


# 2. Reading data from a file
with open("marks.txt", "r") as file:
    data = file.read()

print("Marks:")
print(data)


# 3. Appending data to a file
with open("student.txt", "a") as file:
    name = input("Enter student name: ")
    file.write(name + "\n")


# 4. Reading the appended data
with open("student.txt", "r") as file:
    data = file.read()

print("\nStudent Names:")
print(data)


# 5. Reading file line by line
with open("marks.txt", "r") as file:
    for line in file:
        print("Mark:", line.strip())

