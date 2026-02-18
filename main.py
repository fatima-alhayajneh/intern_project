# بنستورد الكلاس من ملف models
from models import Employee

# إنشاء الموظف الأول
emp1 = Employee("Fatima", "Developer", 1200)

# إنشاء الموظف الثاني
emp2 = Employee("Marco", "Engineer", 1500)

# استدعاء الميثود لعرض البيانات
emp1.display_info()
emp2.display_info()
