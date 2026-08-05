class Car:

    def __init__(self,company,model):
        self.company = company
        self.model = model

    def details(self):
        print(f"Company: {self.company}")
        print(f"Model: {self.model}")

c1 = Car("Toyota", "Camry")
c2 = Car("Honda", "Civic")
c3 = Car("Ford", "Mustang")


c1.details()
c2.details()
c3.details()


class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


e1 = Employee("Arvindra", 50000)
e1.show_salary()