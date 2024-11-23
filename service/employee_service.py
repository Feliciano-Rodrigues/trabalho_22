from repository.employee_repository import EmployeeRepository

class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()

    def create_employee(self, data):
        self.repository.insert(data)
