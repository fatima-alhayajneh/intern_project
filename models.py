class Employee:
    # الـ Constructor اللي بيستقبل البيانات وبخزنها
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    # ميثود لعرض المعلومات بشكل مرتب
    def display_info(self):
        print(f"--- Employee Detail ---")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: ${self.salary}")
        print("-----------------------")
