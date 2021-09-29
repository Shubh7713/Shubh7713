class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

emp = Employee("Shubh agrawal", "1 Million")
emp.info()
print(emp.__dict__)
print(emp.__doc__)
print(emp.__module__)
print(emp.__class__)
