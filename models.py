class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary


    def display_details(self):
        print("--- Employee Detail ---")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: ${self.salary}")
        print("-----------------------")
