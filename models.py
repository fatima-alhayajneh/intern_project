class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def display_info(self):
        print(f"--- Employee Detail ---")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: ${self.salary}")
        print("-----------------------")

class Manager(Employee):
    def __init__(self, name, role, salary, department):
        super().__init__(name, role, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        
