from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, position):
        self._name = name
        self._position = position

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position
    @abstractmethod
    def get_info(self):
        pass
class RegularEmployee(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_info(self):
        return f"Regular Employee: {self.get_name()}, {self.get_position()}, Salary: {self.get_salary()}"


class CRMSystem(ABC):
    def __init__(self):
        self._departments = []

    def get_departments(self):
        return self._departments

    def add_department(self, department):
        self._departments.append(department)

    def get_department_employees(self, department_name):
        for department in self._departments:
            if department.get_name() == department_name:
                return department.get_employees()
        return None

    def __str__(self):
        return f"CRM System с {len(self._departments)} департаментами"

class Department(CRMSystem):
    def __init__(self, name):
        self._name = name
        self._employees = []
    def get_name(self):
        return self._name
    def get_employees(self):
        return self._employees
    def add_employee(self, employee):
        self._employees.append(employee)

    def get_total_salary(self):
        total_salary = sum(employee.get_salary() for employee in self._employees if isinstance(employee, RegularEmployee))
        return total_salary

hr_department = Department("HR")
it_department = Department("IT")

regular_employee = RegularEmployee("Иван", "HR Specialist", 50000)
hr_department.add_employee(regular_employee)

crm_system = CRMSystem()
crm_system.add_department(hr_department)
crm_system.add_department(it_department)

hr_employees = crm_system.get_department_employees("HR")

if hr_employees:
    for employee in hr_employees:
        print(employee.get_info())
else:
    print("Отдел не найден")

print(crm_system)
