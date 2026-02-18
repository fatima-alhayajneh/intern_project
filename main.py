from models import Employee, Manager

def main():
    print("--- Create a Manager Account ---")
    name = input("Enter Name: ")
    role = input("Enter Role: ")
    dept = input("Enter Department: ")
    
    try:
        salary_input = input("Enter Salary: ")
        salary = float(salary_input)
        
        mgr = Manager(name, role, salary, dept)
        mgr.display_info()
        
    except ValueError:
        print("\n[!] Error: Please enter a valid number for salary.")

if __name__ == "__main__":
    main()
