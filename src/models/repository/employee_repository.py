from src.models.entities.employee import Employee

class EmployeeRepository:
    def __init__(self):
        self.starage_employee = [
            {"nome": "admin", "usuario": "admin01@", "senha": "18092024"}
        ]

    def register_employee(self, employee : Employee):
        information_employee = {
            "nome": employee.name,
            "usuario": employee.user,
            "senha": employee.password
        }

        self.starage_employee.append(information_employee)

    def authentication_employee(self, user, password):
        for employee in self.starage_employee:
            if employee["usuario"] == user and employee["senha"] == password:
                return True
        return False
            
    def validate_user_employee(self, user_register):
        for user in self.starage_employee:
            if user["usuario"] == user_register:
                return False
        return True

employee_repository = EmployeeRepository()